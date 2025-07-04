from .models import ClientContext, Config

REFERER_YOUTUBE: str = "https://www.youtube.com/"
REFERER_YOUTUBE_MOBILE: str = "https://m.youtube.com/"
REFERER_YOUTUBE_MUSIC: str = "https://music.youtube.com/"
REFERER_YOUTUBE_KIDS: str = "https://www.youtubekids.com/"
REFERER_YOUTUBE_STUDIO: str = "https://studio.youtube.com/"
REFERER_YOUTUBE_ANALYTICS: str = "https://analytics.youtube.com/"
REFERER_GOOGLE_ASSISTANT: str = "https://assistant.google.com/"

USER_AGENT_WEB: str = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"
)
USER_AGENT_ANDROID: str = (
    "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36"
)
USER_AGENT_IOS: str = (
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/98.2  Mobile/15E148 Safari/605.1.15"
)
USER_AGENT_TV_HTML5: str = (
    "Mozilla/5.0 (PlayStation 4 5.55) AppleWebKit/601.2 (KHTML, like Gecko)"
)
USER_AGENT_TV_APPLE: str = (
    "AppleCoreMedia/1.0.0.12B466 (Apple TV; U; CPU OS 8_1_3 like Mac OS X; en_us)"
)
USER_AGENT_TV_ANDROID: str = (
    "Mozilla/5.0 (Linux; Android 5.1.1; AFTT Build/LVY48F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/49.0.2623.10"
)
USER_AGENT_XBOX_ONE: str = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10553"
)
USER_AGENT_GOOGLE_ASSISTANT: str = (
    "Mozilla/5.0 (Linux; Android 11; Pixel 2; DuplexWeb-Google/1.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Mobile Safari/537.36"
)

config: Config = Config(
    base_url="https://youtubei.googleapis.com/youtubei/v1/",
    clients=[
        ClientContext(
            client_id=1,
            client_name="WEB",
            client_version="2.20250626.01.00",
            user_agent=USER_AGENT_WEB,
            referer=REFERER_YOUTUBE,
            api_key="AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8",
        ),
        ClientContext(
            client_id=2,
            client_name="MWEB",
            client_version="2.20211214.00.00",
            user_agent=USER_AGENT_ANDROID,
            referer=REFERER_YOUTUBE_MOBILE,
            api_key="AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8",
        ),
        ClientContext(
            client_id=3,
            client_name="ANDROID",
            client_version="19.17.34",
            user_agent=USER_AGENT_ANDROID,
            api_key="AIzaSyA8eiZmM1FaDVjRy-df2KTyQ_vz_yYM39w",
        ),
        ClientContext(
            client_id=5,
            client_name="IOS",
            client_version="19.16.3",
            user_agent=USER_AGENT_IOS,
            api_key="AIzaSyB-63vPrdThhKuerbB2N_l7Kwwcxj6yUAc",
        ),
        ClientContext(
            client_id=7,
            client_name="TVHTML5",
            client_version="7.20210224.00.00",
            user_agent=USER_AGENT_TV_HTML5,
            api_key="AIzaSyDCU8hByM-4DrUqRUYnGn-3llEO78bcxq8",
        ),
        ClientContext(
            client_id=8,
            client_name="TVLITE",
            client_version="2",
            user_agent=USER_AGENT_TV_HTML5,
        ),
        ClientContext(
            client_id=10,
            client_name="TVANDROID",
            client_version="1.0",
            user_agent=USER_AGENT_TV_ANDROID,
        ),
        ClientContext(
            client_id=13,
            client_name="XBOXONEGUIDE",
            client_version="1.0",
            user_agent=USER_AGENT_XBOX_ONE,
        ),
        ClientContext(
            client_id=14,
            client_name="ANDROID_CREATOR",
            client_version="21.06.103",
            user_agent=USER_AGENT_ANDROID,
            api_key="AIzaSyD_qjV8zaaUMehtLkrKFgVeSX_Iqbtyws8",
        ),
        ClientContext(
            client_id=15,
            client_name="IOS_CREATOR",
            client_version="20.47.100",
            user_agent=USER_AGENT_IOS,
            api_key="AIzaSyAPyF5GfQI-kOa6nZwO8EsNrGdEx9bioNs",
        ),
        ClientContext(
            client_id=16,
            client_name="TVAPPLE",
            client_version="1.0",
            user_agent=USER_AGENT_TV_APPLE,
        ),
        ClientContext(
            client_id=18,
            client_name="ANDROID_KIDS",
            client_version="7.12.3",
            user_agent=USER_AGENT_ANDROID,
            api_key="AIzaSyAxxQKWYcEX8jHlflLt2Qcbb-rlolzBhhk",
        ),
        ClientContext(
            client_id=19,
            client_name="IOS_KIDS",
            client_version="5.42.2",
            user_agent=USER_AGENT_IOS,
            api_key="AIzaSyA6_JWXwHaVBQnoutCv1-GvV97-rJ949Bc",
        ),
        ClientContext(
            client_id=21,
            client_name="ANDROID_MUSIC",
            client_version="5.01",
            user_agent=USER_AGENT_ANDROID,
            api_key="AIzaSyAOghZGza2MQSZkY_zfZ370N-PUdXEo8AI",
        ),
        ClientContext(
            client_id=23,
            client_name="ANDROID_TV",
            client_version="2.16.032",
            user_agent=USER_AGENT_TV_ANDROID,
        ),
        ClientContext(
            client_id=26,
            client_name="IOS_MUSIC",
            client_version="4.16.1",
            user_agent=USER_AGENT_IOS,
            api_key="AIzaSyBAETezhkwP0ZWA02RsqT1zu78Fpt0bC_s",
        ),
        ClientContext(
            client_id=27,
            client_name="MWEB_TIER_2",
            client_version="9.20220325",
            user_agent=USER_AGENT_ANDROID,
            referer=REFERER_YOUTUBE_MOBILE,
        ),
        ClientContext(
            client_id=28,
            client_name="ANDROID_VR",
            client_version="1.28.63",
            user_agent=USER_AGENT_ANDROID,
        ),
        ClientContext(
            client_id=29,
            client_name="ANDROID_UNPLUGGED",
            client_version="6.13",
            user_agent=USER_AGENT_ANDROID,
        ),
        ClientContext(
            client_id=30,
            client_name="ANDROID_TESTSUITE",
            client_version="1.9",
            user_agent=USER_AGENT_ANDROID,
        ),
        ClientContext(
            client_id=31,
            client_name="WEB_MUSIC_ANALYTICS",
            client_version="0.2",
            user_agent=USER_AGENT_WEB,
            referer=REFERER_YOUTUBE_ANALYTICS,
        ),
        ClientContext(
            client_id=33,
            client_name="IOS_UNPLUGGED",
            client_version="6.13",
            user_agent=USER_AGENT_IOS,
        ),
        ClientContext(
            client_id=38,
            client_name="ANDROID_LITE",
            client_version="3.26.1",
            user_agent=USER_AGENT_ANDROID,
        ),
        ClientContext(
            client_id=39,
            client_name="IOS_EMBEDDED_PLAYER",
            client_version="2.3",
            user_agent=USER_AGENT_IOS,
        ),
        ClientContext(
            client_id=41,
            client_name="WEB_UNPLUGGED",
            client_version="1.20220403",
            user_agent=USER_AGENT_WEB,
            referer=REFERER_YOUTUBE,
        ),
        ClientContext(
            client_id=42,
            client_name="WEB_EXPERIMENTS",
            client_version="1",
            user_agent=USER_AGENT_WEB,
            referer=REFERER_YOUTUBE,
        ),
        ClientContext(
            client_id=43,
            client_name="TVHTML5_CAST",
            client_version="1.1",
            user_agent=USER_AGENT_TV_HTML5,
        ),
        ClientContext(
            client_id=55,
            client_name="ANDROID_EMBEDDED_PLAYER",
            client_version="17.13.3",
            user_agent=USER_AGENT_ANDROID,
            api_key="AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8",
        ),
        ClientContext(
            client_id=56,
            client_name="WEB_EMBEDDED_PLAYER",
            client_version="1.20220413.01.00",
            user_agent=USER_AGENT_WEB,
            referer=REFERER_YOUTUBE,
            api_key="AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8",
        ),
        ClientContext(
            client_id=57,
            client_name="TVHTML5_AUDIO",
            client_version="2.0",
            user_agent=USER_AGENT_TV_HTML5,
        ),
        ClientContext(
            client_id=58,
            client_name="TV_UNPLUGGED_CAST",
            client_version="0.1",
            user_agent=USER_AGENT_TV_HTML5,
        ),
        ClientContext(
            client_id=59,
            client_name="TVHTML5_KIDS",
            client_version="3.20220325",
            user_agent=USER_AGENT_TV_HTML5,
        ),
        ClientContext(
            client_id=60,
            client_name="WEB_HEROES",
            client_version="0.1",
            user_agent=USER_AGENT_WEB,
            referer=REFERER_YOUTUBE,
        ),
        ClientContext(
            client_id=61,
            client_name="WEB_MUSIC",
            client_version="1.0",
            user_agent=USER_AGENT_WEB,
            referer=REFERER_YOUTUBE_MUSIC,
        ),
        ClientContext(
            client_id=62,
            client_name="WEB_CREATOR",
            client_version="1.20210223.01.00",
            user_agent=USER_AGENT_WEB,
            referer=REFERER_YOUTUBE_STUDIO,
            api_key="AIzaSyBUPetSUmoZL-OhlxA7wSac5XinrygCqMo",
        ),
        ClientContext(
            client_id=63,
            client_name="TV_UNPLUGGED_ANDROID",
            client_version="1.22.062.06.90",
            user_agent=USER_AGENT_TV_ANDROID,
        ),
        ClientContext(
            client_id=64,
            client_name="IOS_LIVE_CREATION_EXTENSION",
            client_version="17.13.3",
            user_agent=USER_AGENT_IOS,
        ),
        ClientContext(
            client_id=65,
            client_name="TVHTML5_UNPLUGGED",
            client_version="6.13",
            user_agent=USER_AGENT_TV_HTML5,
        ),
        ClientContext(
            client_id=66,
            client_name="IOS_MESSAGES_EXTENSION",
            client_version="16.20",
            user_agent=USER_AGENT_IOS,
            api_key="AIzaSyDCU8hByM-4DrUqRUYnGn-3llEO78bcxq8",
        ),
        ClientContext(
            client_id=67,
            client_name="WEB_REMIX",
            client_version="1.20230724.00.00",
            user_agent=USER_AGENT_WEB,
            referer=REFERER_YOUTUBE_MUSIC,
            api_key="AIzaSyC9XL3ZjWddXya6X74dJoCTL-WEYFDNX30",
        ),
        ClientContext(
            client_id=68,
            client_name="IOS_UPTIME",
            client_version="1.0",
            user_agent=USER_AGENT_IOS,
        ),
        ClientContext(
            client_id=69,
            client_name="WEB_UNPLUGGED_ONBOARDING",
            client_version="0.1",
            user_agent=USER_AGENT_WEB,
        ),
        ClientContext(
            client_id=70,
            client_name="WEB_UNPLUGGED_OPS",
            client_version="0.1",
            user_agent=USER_AGENT_WEB,
        ),
        ClientContext(
            client_id=71,
            client_name="WEB_UNPLUGGED_PUBLIC",
            client_version="0.1",
            user_agent=USER_AGENT_WEB,
        ),
        ClientContext(
            client_id=72,
            client_name="TVHTML5_VR",
            client_version="0.1",
            user_agent=USER_AGENT_TV_HTML5,
        ),
        ClientContext(
            client_id=74,
            client_name="ANDROID_TV_KIDS",
            client_version="1.16.80",
            user_agent=USER_AGENT_TV_ANDROID,
        ),
        ClientContext(
            client_id=75,
            client_name="TVHTML5_SIMPLY",
            client_version="1.0",
            user_agent=USER_AGENT_TV_HTML5,
        ),
        ClientContext(
            client_id=76,
            client_name="WEB_KIDS",
            client_version="2.20220414.00.00",
            referer=REFERER_YOUTUBE_KIDS,
            user_agent=USER_AGENT_WEB,
            api_key="AIzaSyBbZV_fZ3an51sF-mvs5w37OqqbsTOzwtU",
        ),
        ClientContext(
            client_id=77,
            client_name="MUSIC_INTEGRATIONS",
            client_version="0.1",
        ),
        ClientContext(
            client_id=80,
            client_name="TVHTML5_YONGLE",
            client_version="0.1",
            user_agent=USER_AGENT_TV_HTML5,
        ),
        ClientContext(
            client_id=84,
            client_name="GOOGLE_ASSISTANT",
            client_version="0.1",
            user_agent=USER_AGENT_GOOGLE_ASSISTANT,
        ),
        ClientContext(
            client_id=85,
            client_name="TVHTML5_SIMPLY_EMBEDDED_PLAYER",
            client_version="2.0",
            user_agent=USER_AGENT_TV_HTML5,
        ),
        ClientContext(
            client_id=87,
            client_name="WEB_INTERNAL_ANALYTICS",
            client_version="0.1",
            user_agent=USER_AGENT_WEB,
            referer=REFERER_YOUTUBE_ANALYTICS,
        ),
        ClientContext(
            client_id=88,
            client_name="WEB_PARENT_TOOLS",
            client_version="1.20220403",
            user_agent=USER_AGENT_WEB,
        ),
        ClientContext(
            client_id=89,
            client_name="GOOGLE_MEDIA_ACTIONS",
            client_version="0.1",
            user_agent=USER_AGENT_GOOGLE_ASSISTANT,
        ),
        ClientContext(
            client_id=90,
            client_name="WEB_PHONE_VERIFICATION",
            client_version="1.0.0",
            user_agent=USER_AGENT_WEB,
        ),
        ClientContext(
            client_id=92,
            client_name="IOS_PRODUCER",
            client_version="0.1",
            user_agent=USER_AGENT_IOS,
        ),
        ClientContext(
            client_id=93,
            client_name="TVHTML5_FOR_KIDS",
            client_version="7.20220325",
            user_agent=USER_AGENT_TV_HTML5,
        ),
    ],
)
