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
import bs4
import http.client

from . import enums

from requests import \
(
    Response,
)

class InnerTubeException(Exception):
    '''
    Generic InnerTubeException

    Notes:
        * This exception may also be raised by non-innertube interactions
            (e.g. operations.video_info)
    '''

    def __init__(self, error: dict):
        '''
        Initialise the Exception

        Generates a string representation of the error for use raising the Exception
        '''

        self.error = error

        message = '[{code}] {status}: {message}'.format(**error)

        for sub_error in error.get('errors', ()):
            message += '\n\t{reason}@{domain}: {message}'.format(**sub_error)

        super().__init__(message)

    @classmethod
    def from_response(cls, response: Response):
        content_type = response.headers.get(enums.Header.CONTENT_TYPE.value).lower()

        error = addict.Dict \
        (
            code    = response.status_code,
            status  = response.reason,
            message = http.client.responses[response.status_code],
        )

        if content_type.startswith(enums.Mime.JSON.value):
            error = addict.Dict(response.json()).error or error
        elif content_type.startswith(enums.Mime.HTML.value):
            soup = bs4.BeautifulSoup(response.text, 'html.parser')

            if (title := soup.find('title')):
                error.message = title.text

        return cls(error)
