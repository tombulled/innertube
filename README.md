# innertube
Python Client for Google's Private InnerTube API. Works with: **YouTube**, **YouTube Music**, **YouTube Kids**, **YouTube Studio**

## About
This library handles low-level interactions with the InnerTube API that is used by each of the YouTube services.
Google hasn't made much public about the API, and recently all App interactions use [protobuf](https://github.com/protocolbuffers/protobuf) making them hard to reverse-engineer. The only articles I could find online are:
* [Gizmodo - How Project InnerTube Helped Pull YouTube Out of the Gutter](https://gizmodo.com/how-project-innertube-helped-pull-youtube-out-of-the-gu-1704946491)
* [Fast Company - To Take On HBO And Netflix, YouTube Had To Rewire Itself](https://www.fastcompany.com/3044995/to-take-on-hbo-and-netflix-youtube-had-to-rewire-itself)

## Installation
The `innertube` library uses [Poetry](https://github.com/python-poetry/poetry) and can easily be installed from source, or using *pip*

### From PyPi (using pip)
```console
$ # TODO!
```

### From Source

#### First, clone the repository
```console
$ # Clone the repository
$ git clone https://github.com/tombulled/innertube.git
Cloning into 'innertube'...
done.
$
$ # Enter the repository's directory
$ cd innertube
$
```

#### Installation directly into site-packages
```console
$ # Build the library
$ poetry build
Building innertube
    - Build innertube wheel
$
$ # Install the built wheel
$ pip3 install dist/innertube*.whl
Successfully installed innertube
$
```

#### Installation inside a virtualenv
```console
$ # Install project dependencies
$ poetry install
Installing dependencies from lock file
Installing the current project: innertube
$
$ # To use, either spawn a shell in the virtualenv
$ poetry shell
(innertube-py3.8) $ python3
>>> import innertube
>>>
$
$ # Or... execute Python inside of the virtualenv
$ poetry run python3
>>> import innertube
>>>
$
```

## Usage
```python
>>> import innertube
>>>
>>> # Create a client
>>> client = innertube.client \
(
    device  = innertube.devices.Web,      # Could also be Android etc.
    service = innertube.services.YouTube, # Could also be YouTubeMusic etc.
)
>>>
>>> # Or... just import the specific one you want
>>> client = innertube.clients.Web()
>>>
>>> # View the client
>>> client
<Client(device='Web', service='YouTube')>
>>>
>>> # Get some data!
>>> data = client.search(query = 'foo fighters')
>>>
>>> # Power user? No problem, dispatch requests yourself
>>> data = client('browse', payload = {'browseId': 'FEwhat_to_watch'})
>>>
>>> # The core endpoints are implemented, so the above is equivalent to:
>>> data = client.browse(browse_id = 'FEwhat_to_watch') # A bit cleaner ;)
```

## Why not just use the [YouTube Data API](https://developers.google.com/youtube/v3/)?
It's entirely up to you and your needs, however this library provides functionality you wont get from the Data API, but it comes at somewhat of a cost *(explained below)*
|                                       | This Library | YouTube Data API |
| ------------------------------------- | ------------ | ---------------- |
| No Google account required            | &check;      | &cross;          |
| No request limit                      | &check;      | &cross;          |
| Clean, reliable, well-structured data | &cross;      | &check;          |

### Wait a sec! What do you mean it's not clean, reliable and well-structured??
Well, the private InnerTube API is not designed for consumption by users, it is used to render and operate the various YouTube services.

### What does that mean?
Simply put, the data returned by the InnerTube API will need to be parsed and sanitised to extract the usable data as it will contain a lot of fluff that is unlikely to be of any use. These higher-level clients are in the works!

## Clients
This table shows all the devices and services that work with the InnerTube API. For example, you could query the API as if you were using the YouTube app on your Tv!
|         | YouTube | YouTubeMusic | YouTubeKids | YouTubeStudio |
| ------- | ------- | ------------ | ----------- | ------------- |
| Web     | &check; | &check;      | &check;     | &check;       |
| Android | &check; | &check;      | &check;     | &check;       |
| Ios     | &check; | &check;      | &check;     | &check;       |
| Tv      | &check; | &cross;      | &cross;     | &cross;       |

## Endpoints
Only the core, unauthenticated endpoints are currently implemented. However, between all of these you should be able to access all the data you need.
|                                | YouTube | YouTubeMusic | YouTubeKids | YouTubeStudio |
| ------------------------------ | ------- | ------------ | ----------- | ------------- |
| config                         | &check; | &check;      | &check;     | &check;       |
| browse                         | &check; | &check;      | &check;     | &check;       |
| player                         | &check; | &check;      | &check;     | &check;       |
| next                           | &check; | &check;      | &check;     | &cross;       |
| search                         | &check; | &check;      | &check;     | &cross;       |
| guide                          | &check; | &check;      | &cross;     | &cross;       |
| music/get_search_suggestions   | &cross; | &check;      | &cross;     | &cross;       |
| music/get_queue                | &cross; | &check;      | &cross;     | &cross;       |

## What about Authentication?
The InnerTube API uses OAuth2, however I have been unable to successfully implement authentication.
Therefore, this library currently only provides unauthenticated access to the API.
