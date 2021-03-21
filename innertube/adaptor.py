'''
Library containing an `Adaptor` for use dispatching requests to the InnerTube API

Usage:
    >>> from innertube.adaptor import Adaptor
    >>>
    >>> Adaptor(my_client_info)
    ...
    >>>
'''

import requests
import bs4
import babel
import addict
import simplejson.errors
import copy
import http.client

from . import utils
from . import errors

from typing import \
(
    Union,
)

from .infos.models import \
(
    ClientInfo,
)

from babel import \
(
    Locale,
)

class Adaptor(object):
    '''
    An adaptor for use dispatching requests to the InnerTube API

    Unlike a `Client`, the adaptor is responsible for facilitating the communication
    process with the API. This includes, setting appropriate headers, applying the
    client context to the request and other such tasks.

    This class allows Clients to remain purely client-focused and not have to
    worry about managing the requests themselves.
    '''

    client_info: ClientInfo
    locale:      Locale

    __session:      requests.Session
    __visitor_data: Union[str, None] = None

    def __init__ \
            (
                self,
                client_info: ClientInfo,
                *,
                locale: Locale = None,
            ):
        '''
        Initialise the adaptor with the provided ClientInfo
        '''

        self.session     = requests.Session()
        self.locale      = locale or babel.Locale('en', 'GB')
        self.client_info = client_info

    def __repr__(self) -> str:
        '''
        Return a string representation of the adaptor
        '''

        return '<{class_name}({params})>'.format \
        (
            class_name  = self.__class__.__name__,
            params = ', '.join \
            (
                f'{key}={value!r}'
                for key, value in \
                {
                    'client': self.client_info.name,
                    'host':   self.client_info.api.domain,
                    'locale': self.client_context.hl,
                }.items()
            )
        )

    @property
    def session(self) -> requests.Session:
        '''
        Return the adaptor's Session (requests.Session)

        Updates the headers used by the session with information such as the
        client name and version
        '''

        self.__session.headers.update \
        (
            utils.filter \
            (
                {
                    # Native Headers
                    'User-Agent': self.client_info.user_agent,
                    'Referer':    utils.url(domain = self.client_info.service.domain),

                    # Custom Headers
                    'X-Goog-Visitor-Id':        self.__visitor_data,
                    'X-YouTube-Client-Name':    str(self.client_info.service.id),
                    'X-YouTube-Client-Version': self.client_info.version,
                }
            )
        )

        return self.__session

    @session.setter
    def session(self, value: requests.Session):
        '''
        Set the adaptor's Session (requests.Session)
        '''

        self.__session = value

    @property
    def params(self) -> addict.Dict:
        '''
        Generate request parameters including the Client's API Key
        '''

        return addict.Dict \
        (
            key = self.client_info.api.key,
            alt = 'json',
        )

    @property
    def client_context(self) -> addict.Dict:
        '''
        Generate the client's context, which is used in the request payload
        '''

        return addict.Dict \
        (
            # Client
            clientName    = self.client_info.name,
            clientVersion = self.client_info.version,

            # Localisation
            gl = self.locale.territory,
            hl = '-'.join \
            (
                utils.filter \
                (
                    (
                        self.locale.language,
                        self.locale.territory,
                    ),
                ),
            ),
        )

    def url(self, endpoint: str) -> str:
        '''
        Generate an API URL using the provided endpoint
        '''

        return utils.url \
        (
            domain   = self.client_info.api.domain,
            endpoint = 'youtubei/v{api_version}/{endpoint}'.format \
            (
                api_version = self.client_info.api.version,
                endpoint    = endpoint.lstrip(r'\/'),
            ),
        )

    def dispatch(self, endpoint: str, payload: dict = {}, params: dict = {}) -> dict:
        '''
        Dispatch a request to the API

        Notes:
            * The client's context is automatically added to the payload
            * If the response is not JSON, an InnerTubeException is raised
        '''

        payload = copy.deepcopy(payload)
        params  = copy.deepcopy(params)

        params.update(self.params)

        payload.setdefault('context', {})

        payload['context']['client'] = \
        {
            **self.client_context,
            **payload.get('context').get('client', {}),
        }

        response = self.session.post \
        (
            url     = self.url(endpoint),
            params  = params,
            json    = payload,
            timeout = 5,
        )

        try:
            data = response.json()
        except simplejson.errors.JSONDecodeError:
            message = http.client.responses[response.status_code]

            try:
                soup = bs4.BeautifulSoup(response.text, 'html.parser')

                if (title := soup.find('title')):
                    message = title.text
            except:
                pass

            raise errors.InnerTubeException \
            (
                {
                    'code':    response.status_code,
                    'status':  response.reason,
                    'message': message
                }
            ) from None

        if (error := data.get('error')):
            raise errors.InnerTubeException(error)

        if (visitor_data := data.get('responseContext', {}).get('visitorData')):
            self.__visitor_data = visitor_data

        return data
