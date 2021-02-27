class InnerTubeException(Exception):
    def __init__(self, error: dict):
        self.error = error

        message = '[{code}] {status}: {message}'.format(**error)

        for sub_error in error.get('errors', ()):
            message += '\n\t{reason}@{domain}: {message}'.format(**sub_error)

        super().__init__(message)
