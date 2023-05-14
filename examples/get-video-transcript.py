from innertube import InnerTube

PANEL_IDENTIFIER_TRANSCRIPT = "engagement-panel-searchable-transcript"


def extract_transcript_params(next_data):
    engagement_panels = next_data["engagementPanels"]

    for engagement_panel in engagement_panels:
        engagement_panel_section = engagement_panel[
            "engagementPanelSectionListRenderer"
        ]

        if (
            engagement_panel_section.get("panelIdentifier")
            != PANEL_IDENTIFIER_TRANSCRIPT
        ):
            continue

        return engagement_panel_section["content"]["continuationItemRenderer"][
            "continuationEndpoint"
        ]["getTranscriptEndpoint"]["params"]


video_id = "5qQ_PJEnrV0"

client = InnerTube("WEB")

data = client.next(video_id)

transcript_params = extract_transcript_params(data)

transcript = client.get_transcript(transcript_params)

transcript_segments = transcript["actions"][0]["updateEngagementPanelAction"]["content"][
    "transcriptRenderer"
]["content"]["transcriptSearchPanelRenderer"]["body"]["transcriptSegmentListRenderer"][
    "initialSegments"
]

for transcript_segment in transcript_segments:
    transcript_segment_renderer = transcript_segment["transcriptSegmentRenderer"]

    start_time = transcript_segment_renderer["startTimeText"]["simpleText"]
    snippet = transcript_segment_renderer["snippet"]["runs"][0]["text"]

    print(f"[{start_time}] {snippet}")
