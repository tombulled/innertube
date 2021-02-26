# innertube
Python Client for Google's InnerTube API (works with YouTube, YouTube Music etc.)

### Clients
|         | YouTube | YouTube Music | YouTube Kids | YouTube Studio  |
| ------- | ------- | ------------- | ------------ | --------------- |
| Web     | WEB     | WEB_REMIX     | WEB_KIDS     | WEB_CREATOR     |
| Android | ANDROID | ANDROID_MUSIC | ANDROID_KIDS | ANDROID_CREATOR |
| Ios     | IOS     | IOS_MUSIC     | IOS_KIDS     | IOS_CREATOR     |

### Authentication
The InnerTube API uses OAuth2, however I have been unable to successfully request tokens.
Therefore, this library provides unauthenticated access to the API.
As YouTube Studio requires authentication, it is inaccessible.


# NOTES
TODO:
* Get OAuth working this time -- nope :/
* Can the protobuf be decoded? -- not going to try :/
* Will installing an old apk version still use the json api? -- hopefully!
