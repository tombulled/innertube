# innertube
Python Client for Google's Private InnerTube API (works with YouTube, YouTube Music etc.)

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
>>> # View the client
>>> client
<Client(device='Web', service='YouTube')>
>>>
>>> # Get some data!
>>> data = client.search(query = 'foo fighters')
>>>
```

### Clients
|         | YouTube | YouTubeMusic | YouTubeKids | YouTubeStudio |
| ------- | ------- | ------------ | ----------- | ------------- |
| Web     | &check; | &check;      | &check;     | &check;       |
| Android | &check; | &check;      | &check;     | &check;       |
| Ios     | &check; | &check;      | &check;     | &check;       |
| Tv      | &check; | &cross;      | &cross;     | &cross;       |

### Authentication
The InnerTube API uses OAuth2, however I have been unable to successfully implement authentication.
Therefore, this library currently only provides unauthenticated access to the API.
