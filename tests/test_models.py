from innertube.models import ResponseContext
import addict


def test_response_context() -> None:
    raw_response_context: dict = {
        "visitorData": "CgtJUDBQUHhYUE8yQSjy9OqSBg%3D%3D",
        "serviceTrackingParams": [
            {
                "service": "CSI",
                "params": [
                    {"key": "c", "value": "WEB"},
                    {"key": "cver", "value": "2.20210223.09.00"},
                    {"key": "yt_li", "value": "0"},
                    {"key": "GetWebMainAppGuide_rid", "value": "0xb0c4a6d9e0681823"},
                ],
            },
            {
                "service": "GFEEDBACK",
                "params": [
                    {"key": "logged_in", "value": "0"},
                    {
                        "key": "e",
                        "value": "24077266,24172383,23735347,24176755,24138064,24002025,24200174,24189899,23804281,23946420,24077241,24004644,24174213,24007246,24199774,24198106,24161848,23998056,24169500,24193864,23934970,24187043,24177193,24145515,24157363,1714248,24167385,24198821,24135310,24185614,24085811,24187377,24140247,23983296,23848212,24138442,24036947,24164186,24106839,24180089,24034168,24189367,24197047,24198104,24120819,39321475,24163012,24191629,24148481,23882685,24062269,24001373,24152442,23918597,24170045,24002022,24166867,24165080,24197650,24166442,23744176,9407156,24168749,24175488,24162650,24186023,24082662,24181174,24185349,24196776,24080738,24187516,23966208,24186508,24130897,23986019",
                    },
                ],
            },
            {"service": "GUIDED_HELP", "params": [{"key": "logged_in", "value": "0"}]},
            {
                "service": "ECATCHER",
                "params": [
                    {"key": "client.version", "value": "2.20211103"},
                    {"key": "client.name", "value": "WEB"},
                    {
                        "key": "client.fexp",
                        "value": "24077266,24172383,23735347,24176755,24138064,24002025,24200174,24189899,23804281,23946420,24077241,24004644,24174213,24007246,24199774,24198106,24161848,23998056,24169500,24193864,23934970,24187043,24177193,24145515,24157363,1714248,24167385,24198821,24135310,24185614,24085811,24187377,24140247,23983296,23848212,24138442,24036947,24164186,24106839,24180089,24034168,24189367,24197047,24198104,24120819,39321475,24163012,24191629,24148481,23882685,24062269,24001373,24152442,23918597,24170045,24002022,24166867,24165080,24197650,24166442,23744176,9407156,24168749,24175488,24162650,24186023,24082662,24181174,24185349,24196776,24080738,24187516,23966208,24186508,24130897,23986019",
                    },
                ],
            },
        ],
        "maxAgeSeconds": 3600,
        "mainAppWebResponseContext": {"loggedOut": True},
        "webResponseContextExtensionData": {"hasDecorated": True},
    }

    response_context: ResponseContext = ResponseContext.parse(
        addict.Dict(raw_response_context)
    )

    assert response_context == ResponseContext(
        function=None,
        browse_id=None,
        context=None,
        visitor_data="CgtJUDBQUHhYUE8yQSjy9OqSBg%3D%3D",
        client=ResponseContext.Client(name="WEB", version="2.20210223.09.00"),
        request=ResponseContext.Request(
            type="WebMainAppGuide", id="0xb0c4a6d9e0681823"
        ),
        flags=ResponseContext.Flags(logged_in=False),
    )
