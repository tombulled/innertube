import requests
import bs4
# import json
import simplejson.errors
import copy
from typing import Union
import http.client
from . import utils
from . import errors
from .infos.models import ClientInfo

class Adaptor(object):
    client_info: ClientInfo

    __session: requests.Session
    __visitor_data: Union[str, None] = None

    def __init__(self, client_info: ClientInfo):
        self.client_info = client_info

        self.session = requests.Session()

    def __repr__(self):
        return '<{class_name}(client={client_name!r}, host={api_domain!r})>'.format \
        (
            class_name  = self.__class__.__name__,
            client_name = self.client_info.name,
            api_domain  = self.client_info.api.domain,
        )

    @property
    def session(self):
        self.__session.headers.update \
        (
            utils.filter \
            (
                {
                    'User-Agent': self.client_info.user_agent,
                    'Referer': utils.url \
                    (
                        domain = self.client_info.service.domain,
                    ),
                    'X-Goog-Visitor-Id': self.__visitor_data,
                }
            )
        )

        return self.__session

    @session.setter
    def session(self, value: requests.Session):
        self.__session = value

    @property
    def params(self):
        return \
        {
            'key': self.client_info.api.key,
            'alt': 'json',
        }

    @property
    def client_context(self):
        return \
        {
            'clientName':    self.client_info.name,
            'clientVersion': self.client_info.version,
            'gl': 'US',
            'hl': 'en',
        }

    def url(self, endpoint: str):
        return utils.url \
        (
            domain   = self.client_info.api.domain,
            endpoint = 'youtubei/v{api_version}/{endpoint}'.format \
            (
                api_version = self.client_info.api.version,
                endpoint    = endpoint.lstrip(r'\/'),
            ),
        )

    def dispatch(self, endpoint: str, payload: dict = {}, params: dict = {}):
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
            timeout = 5, # NOTE: This should probably be a constant/configurable (is it still needed?)
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

        error = data.get('error')

        if error:
            raise errors.InnerTubeException(error)

        if (visitor_data := data.get('responseContext', {}).get('visitorData')):
            self.__visitor_data = visitor_data

        return data
