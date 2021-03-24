'''
Library containing custom Exceptions

>>> from innertube import errors
>>>
>>> dir(errors)
...
>>>
>>> raise errors.InnerTubeException \
(
    {
        'code':    501,
        'status':  'UNIMPLEMENTED',
        'message': 'Operation is not implemented, or supported, or enabled.'
    }
)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
innertube.errors.InnerTubeException: [501] UNIMPLEMENTED: Operation is not implemented, or supported, or enabled.
>>>
'''

import addict
import attr
import bs4

import http.client

from . import enums
from . import models

from requests import \
(
    Response,
)

@attr.s
class InnerTubeException(Exception):
    '''
    Generic InnerTubeException

    Notes:
        * This exception may also be raised by non-innertube interactions
            (e.g. operations.video_info)
    '''

    error: models.Error = attr.ib()

    def __str__(self) -> str:
        return '\n\t'.join \
        (
            (
                f'[{self.error.code}] {self.error.status}: {self.error.message}',
                * \
                (
                    f'{error.reason}@{error.domain}: {error.message}'
                    for error in self.error.errors or ()
                ),
            ),
        )

    @classmethod
    def from_response(cls, response: Response):
        content_type = response.headers.get(enums.Header.CONTENT_TYPE.value).lower()

        error_message = http.client.responses[response.status_code]

        if content_type.startswith(enums.Mime.JSON.value):
            data = addict.Dict(response.json())

            if (error := data.error):
                return cls(models.Error(**error))
        elif content_type.startswith(enums.Mime.HTML.value):
            soup = bs4.BeautifulSoup(response.text, 'html.parser')

            if (title := soup.find('title')):
                error_message = title.text

        return cls \
        (
            models.Error \
            (
                code    = response.status_code,
                status  = response.reason,
                message = error_message,
            )
        )
