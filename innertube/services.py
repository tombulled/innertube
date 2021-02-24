from pydantic import BaseModel

class Client(BaseModel):
    name:    str
    version: str

class Api(BaseModel):
    key:     str
    domain:  str
    version: int

class Adaptor(BaseModel):
    user_agent: str
    origin:     str

class Service(BaseModel):
    client:  Client
    api:     Api
    adaptor: Adaptor

Web = Service \
(
    client = Client \
    (
        name    = 'WEB',
        version = '2.20200516.07.00',
    ),
    api = Api \
    (
        key     = 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
        domain  = 'youtubei.googleapis.com',
        version = 1,
    ),
    adaptor = Adaptor \
    (
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        origin     = 'www.youtube.com',
    ),
)

WebRemix = Service \
(
    client = Client \
    (
        name    = 'WEB_REMIX',
        version = '0.1',
    ),
    api = Api \
    (
        key     = 'AIzaSyC9XL3ZjWddXya6X74dJoCTL-WEYFDNX30',
        domain  = 'youtubei.googleapis.com',
        version = 1,
    ),
    adaptor = Adaptor \
    (
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        origin     = 'music.youtube.com',
    ),
)
