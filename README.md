# innertube
Python Client for Google's Private InnerTube API. Works with: **YouTube**, **YouTube Music**, **YouTube Kids**, **YouTube Studio**

### About
I initially created a [YouTube Music Web API Client](https://github.com/tombulled/python-youtube-music), however I failed miserably to follow the [KISS](https://en.m.wikipedia.org/wiki/KISS_principle) principle. Therefore, I created this package to handle low-level interactions with the InnerTube API that works with each of the YouTube services!

### Installation
```shell
$ foo...
```

### Usage
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

### But, why not just use the [YouTube Data API](https://developers.google.com/youtube/v3/)?
Go for it! Unless you want unlimited unauthenticated requests...
In all seriousness, this library provides functionality you wont get from the Data API, but it comes at somewhat of a cost *(explained below)*
|                                       | This Library | YouTube Data API |
| ------------------------------------- | ------------ | ---------------- |
| No Google account required            | &check;      | &cross;          |
| No request limit                      | &check;      | &cross;          |
| Clean, reliable, well-structured data | &cross;      | &check;          |

#### Wait a sec! What do you mean it's not clean, reliable and well-structured??
Well, the private InnerTube API is not designed for consumption by users, it is used to render and operate the various YouTube services.

#### What does that mean?
Simply put, the data returned by the InnerTube API will need to be parsed and sanitised to extract the usable data as it will contain a lot of fluff that is unlikely to be of any use. These higher-level clients are in the works!

### Clients
This table shows all the devices and services that work with the InnerTube API. For example, you could query the API as if you were using the YouTube app on your Tv!
|         | YouTube | YouTubeMusic | YouTubeKids | YouTubeStudio |
| ------- | ------- | ------------ | ----------- | ------------- |
| Web     | &check; | &check;      | &check;     | &check;       |
| Android | &check; | &check;      | &check;     | &check;       |
| Ios     | &check; | &check;      | &check;     | &check;       |
| Tv      | &check; | &cross;      | &cross;     | &cross;       |

### Endpoints
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

### What about Authentication?
The InnerTube API uses OAuth2, however I have been unable to successfully implement authentication.
Therefore, this library currently only provides unauthenticated access to the API.
