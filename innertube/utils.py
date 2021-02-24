from typing import Union

def url(*, domain: str, scheme: str = 'https', port: Union[int, None] = None, endpoint: Union[str, None] = None):
    return '{scheme}://{domain}{sep_port}{port}/{endpoint}'.format \
    (
        scheme   = scheme,
        domain   = domain,
        sep_port = ':' if port else '',
        port     = port or '',
        endpoint = endpoint.lstrip(r'\/') if endpoint else '',
    )
