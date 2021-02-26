# innertube
Python Client for Google's InnerTube API (works with YouTube, YouTube Music etc.)

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
    service = innertube.services.YouTube, # Could also be YouTubeMusic etc.
    device  = innertube.devices.Web,      # Could also be Android etc.
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
|         | YouTube | YouTube Music | YouTube Kids | YouTube Studio  |
| ------- | ------- | ------------- | ------------ | --------------- |
| Web     | WEB     | WEB_REMIX     | WEB_KIDS     | WEB_CREATOR     |
| Android | ANDROID | ANDROID_MUSIC | ANDROID_KIDS | ANDROID_CREATOR |
| Ios     | IOS     | IOS_MUSIC     | IOS_KIDS     | IOS_CREATOR     |
| Tv      | TVHTML5 | N/A           | N/A          | N/A             |

### Authentication
The InnerTube API uses OAuth2, however I have been unable to successfully request tokens.
Therefore, this library provides unauthenticated access to the API.


# TEMP NOTES
TODO:
* Take out free trials again?
