from innertube import InnerTube
from innertube.raw_models import ResponseContext

WEB = InnerTube("WEB", "2.20230728.00.00")
WEB_REMIX = InnerTube("WEB_REMIX", "1.20220607.03.01")
IOS = InnerTube("IOS", "17.14.2")
IOS_MUSIC = InnerTube("IOS_MUSIC", "4.16.1")

channel_id: str = "UC8Yu1_yfN5qPh601Y4btsYw"  # Arctic Monkeys

d = data = WEB_REMIX.adaptor.dispatch("browse", body={"browseId": channel_id})

rc = ResponseContext.parse_obj(data["responseContext"])
