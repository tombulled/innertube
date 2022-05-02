# innertube
Python Client for Google's Private InnerTube API. Works with **YouTube**, **YouTube Music**, **YouTube Kids**, **YouTube Studio** and more!

## About
This library handles low-level interactions with the underlying InnerTube API used by each of the YouTube services.

Here are a few articles available online relating to the InnerTube API:
* [Gizmodo - How Project InnerTube Helped Pull YouTube Out of the Gutter](https://gizmodo.com/how-project-innertube-helped-pull-youtube-out-of-the-gu-1704946491)
* [Fast Company - To Take On HBO And Netflix, YouTube Had To Rewire Itself](https://www.fastcompany.com/3044995/to-take-on-hbo-and-netflix-youtube-had-to-rewire-itself)

## Installation
`innertube` uses [Poetry](https://github.com/python-poetry/poetry) under the hood and can easily be installed from source or from PyPI using *pip*.

### Latest Release
```console
pip install innertube
```

### Bleeding Edge
```console
pip install git+https://github.com/tombulled/innertube@develop
```

## Usage
```python
>>> import innertube
>>>
>>> # Construct a client
>>> client = innertube.InnerTube("WEB")
>>>
>>> # Get some data!
>>> data = client.search(query="foo fighters")
>>>
>>> # Power user? No problem, dispatch requests yourself
>>> data = client("browse", body={"browseId": "FEwhat_to_watch"})
>>>
>>> # The core endpoints are implemented, so the above is equivalent to:
>>> data = client.browse("FEwhat_to_watch")
```

## Comparison with the [YouTube Data API](https://developers.google.com/youtube/v3/)
The InnerTube API provides access to data you can't get from the Data API, however it comes at somewhat of a cost *(explained below)*.
|                                       | This Library | YouTube Data API |
| ------------------------------------- | ------------ | ---------------- |
| Google account required               | No           | Yes              |
| Request limit                         | No           | Yes              |
| Clean data                            | No           | Yes              |

As the InnerTube API is used by the variety of YouTube services and is not designed for consumption by users. Therefore, the data returned by the InnerTube API will need to be parsed and sanitised to extract data of interest.

## Endpoints
Currently only the following core, unauthenticated endpoints are implemented:
|                                | YouTube | YouTubeMusic | YouTubeKids | YouTubeStudio |
| ------------------------------ | ------- | ------------ | ----------- | ------------- |
| config                         | &check; | &check;      | &check;     | &check;       |
| browse                         | &check; | &check;      | &check;     | &check;       |
| player                         | &check; | &check;      | &check;     | &check;       |
| next                           | &check; | &check;      | &check;     |               |
| search                         | &check; | &check;      | &check;     |               |
| guide                          | &check; | &check;      |             |               |
| music/get_search_suggestions   |         | &check;      |             |               |
| music/get_queue                |         | &check;      |             |               |

## Authentication
The InnerTube API uses OAuth2, however this has not yet been implemented, therefore this library currently only provides unauthenticated API access.