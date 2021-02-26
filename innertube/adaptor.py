import requests
import json

from . import utils
from . import exceptions

from .infos.models import ClientInfo
from typing import Union

class Adaptor(object):
    # Public attributes
    client_info: ClientInfo

    # Properties
    __session: requests.Session

    # Private attributes
    __visitor_data: Union[str, None] = None

    def __init__(self, client_info: ClientInfo):
        self.client_info = client_info

        self.session = requests.Session()

    def __repr__(self):
        return f'<{self.__class__.__name__}({self.client_info.name}@{self.client_info.api.domain})>'

    @property
    def session(self):
        self.__session.headers.update \
        (
            utils.filter \
            (
                {
                    'User-Agent': self.user_agent,
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
    def user_agent(self):
        return utils.build_user_agent(self.client_info)

    @property
    def params(self):
        return \
        {
            'key': self.client_info.api.key,
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
                    'clientName':    self.client_info.name,
                    'clientVersion': self.client_info.version,
                    'gl': 'US',
                    'hl': 'en',
                },
            },
        }

    def url(self, *fragments: str):
        return utils.url \
        (
            domain   = self.client_info.api.domain,
            endpoint = '/'.join \
            (
                fragment.lstrip(r'\/')
                for fragment in \
                (
                    f'youtubei/v{self.client_info.api.version}',
                    *fragments,
                )
            ),
        )

    def dispatch(self, *fragments: str, params: dict = {}, payload: dict = {}):
        url = self.url(*fragments)

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
