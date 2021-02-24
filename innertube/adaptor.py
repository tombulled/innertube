import requests

from . import utils
from . import exceptions

# Typing
from .services import Service
from typing import Union

class Adaptor(object):
    # Public attributes
    service: Service

    # Properties
    __session: requests.Session

    # Private attributes
    __visitor_data: Union[str, None] = None

    def __init__(self, service: Service):
        self.service = service

        self.session = requests.Session()

    def __repr__(self):
        return f'<{self.__class__.__name__}({self.service.client.name}@{self.service.api.domain})>'

    @property
    def session(self):
        self.__session.headers.update \
        (
            utils.filter \
            (
                {
                    'User-Agent': self.service.adaptor.user_agent,
                    'Referer': utils.url \
                    (
                        domain = self.service.adaptor.origin,
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
            'key': self.service.api.key,
            'alt': 'json',
        }

    @property
    def payload(self):
        return \
        {
            'context': \
            {
                'client': \
                {
                    'clientName':    self.service.client.name,
                    'clientVersion': self.service.client.version,
                    'gl': 'US',
                    'hl': 'en',
                },
            },
        }

    def _url(self, *fragments: str):
        return utils.url \
        (
            domain   = self.service.api.domain,
            endpoint = '/'.join \
            (
                fragment.lstrip(r'\/')
                for fragment in \
                (
                    f'youtubei/v{self.service.api.version}',
                    *fragments,
                )
            ),
        )

    def dispatch(self, *fragments: str, params: dict = {}, payload: dict = {}):
        url = self._url(*fragments)

        params  = {**self.params,  **params}
        payload = {**self.payload, **payload}

        response = self.session.post \
        (
            url     = url,
            params  = params,
            json    = payload,
            timeout = 5, # NOTE: This should be a constant/configurable
        )

        try:
            data = response.json()
        except json.JSONDecodeError:
            raise # TODO: Handle gracefully

        error = data.get('error')

        if error:
            raise exceptions.InnertubeException(error)

        visitor_data = data.get('responseContext', {}).get('visitorData')

        if visitor_data: self.__visitor_data = visitor_data

        return data
