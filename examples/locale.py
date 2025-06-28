from innertube import InnerTube
from innertube.locale import Language, Locale, Location
from innertube.enums import BrowseId

client: InnerTube = InnerTube(
    client_name="WEB",
    locale=Locale(
        language=Language.KOREAN,
        location=Location.SOUTH_KOREA,
    ),
)

data = client.browse(BrowseId.WHAT_TO_WATCH)
