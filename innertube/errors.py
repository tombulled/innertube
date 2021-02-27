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
