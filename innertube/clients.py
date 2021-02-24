import requests

from . import utils

# Typing
from .services import Service

class Client(object):
    service: Service

    # Properties
    __session: requests.Session

    def __init__(self, service: Service):
        self.service = service

        self.session = requests.Session()

    @property
    def session(self):
        self.__session.headers.update \
        (
            {
                'Referer': utils.url \
                (
                    domain = self.service.adaptor.origin,
                )
            }
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

        print(self.params)

        params  = {**self.params,  **params}
        payload = {**self.payload, **payload}

        response = self.session.post \
        (
            url     = url,
            params  = params,
            json    = payload,
            # timeout = 5, # This should be a constant/configurable
        )

        return response.json()

        # try:
        #     data = response.json()
        # except json.JSONDecodeError:
        #     raise # Raise custom exception?
        #
        # error = data.get('error')
        #
        # if error:
        #     raise exceptions.ApiError(error)
        #
        # if 'responseContext' in data:
        #     response_context = data['responseContext']
        #
        #     if 'visitorData' in response_context:
        #         visitor_data = response_context['visitorData']
        #
        #         self.visitor_data = visitor_data
        #
        # return data
