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
import addict
import furl

from . import utils
from . import errors
from . import enums
from . import constants

from typing import \
(
    Optional,
)

from .models import \
(
    AppInfo,
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

    info:   AppInfo
    locale: Locale

    __session:      requests.Session
    __visitor_data: Optional[str] = None

    def __init__ \
            (
                self,
                info: AppInfo,
                *,
                locale: Locale = None,
            ):
        '''
        Initialise the adaptor with the provided AppInfo
        '''

        self.session = requests.Session()
        self.locale  = locale or constants.DEFAULT_LOCALE
        self.info    = info

    def __repr__(self) -> str:
        '''
        Return a string representation of the adaptor
        '''

        return utils.repr \
        (
            class_name = self.__class__.__mro__[-2].__name__,
            fields     = dict \
            (
                client = self.info.client.name,
                host   = self.info.api.domain,
                locale = self.context.hl,
            ),
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
                    enums.Header.USER_AGENT.value:     self.info.user_agent,
                    enums.Header.REFERER.value:        utils.url(domain = self.info.service.domain),
                    enums.Header.VISITOR_ID.value:     self.visitor_data,
                    enums.Header.CLIENT_NAME.value:    str(self.info.service.id),
                    enums.Header.CLIENT_VERSION.value: self.info.client.version,
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
            key = self.info.api.key,
            alt = enums.Alt.JSON.value,
        )

    @property
    def context(self) -> addict.Dict:
        '''
        Generate the client's context, which is used in the request payload
        '''

        return addict.Dict \
        (
            clientName    = self.info.client.name,
            clientVersion = self.info.client.version,
            gl            = self.locale.territory,
            hl            = '-'.join \
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

    @property
    def visitor_data(self) -> Optional[str]:
        return self.__visitor_data

    def url(self, endpoint: str) -> furl.furl:
        '''
        Generate an API URL using the provided endpoint
        '''

        endpoint = endpoint.lstrip(r'\/')

        return furl.furl \
        (
            scheme = enums.Scheme.HTTPS.value,
            host   = self.info.api.domain,
            path   = furl.Path() / 'youtubei' / f'v{self.info.api.version}' / endpoint,
        )

    def dispatch \
            (
                self,
                endpoint: str,
                payload:  Optional[dict] = None,
                params:   Optional[dict] = None,
            ) -> addict.Dict:
        '''
        Dispatch a request to the API

        Notes:
            * The client's context is automatically added to the payload
            * If the response is erroneous, an InnerTubeException is raised
        '''

        params = addict.Dict \
        (
            ** \
            (
                utils.filter(params)
                if params
                else {}
            ),
            **self.params,
        )

        payload = addict.Dict \
        (
            utils.filter(payload)
            if payload
            else {}
        )

        payload.context.client.update(self.context)

        response = self.session.post \
        (
            url     = self.url(endpoint),
            params  = params,
            json    = payload,
        )

        if not response.ok:
            raise errors.InnerTubeException.from_response(response) from None

        data = addict.Dict(response.json())

        if (visitor_data := data.responseContext.visitorData):
            self.__visitor_data = visitor_data

        return data
