from innertube import InnerTube

ENGAGEMENT_SECTION_COMMENTS = "engagement-panel-comments-section"
C0MMENTS_TOP = "Top comments"
COMMENTS_NEWEST = "Newest first"


def parse_text(text):
    return "".join(run["text"] for run in text["runs"])


def extract_engagement_panels(next_data):
    engagement_panels = {}
    raw_engagement_panels = next_data.get("engagementPanels", [])

    for raw_engagement_panel in raw_engagement_panels:
        engagement_panel = raw_engagement_panel.get(
            "engagementPanelSectionListRenderer", {}
        )
        target_id = engagement_panel.get("targetId")

        engagement_panels[target_id] = engagement_panel

    return engagement_panels


def parse_sort_filter_sub_menu(menu):
    menu_items = menu["sortFilterSubMenuRenderer"]["subMenuItems"]

    return {menu_item["title"]: menu_item for menu_item in menu_items}


def extract_comments(next_continuation_data):
    return [
        continuation_item["commentThreadRenderer"]
        for continuation_item in next_continuation_data["onResponseReceivedEndpoints"][
            1
        ]["reloadContinuationItemsCommand"]["continuationItems"][:-1]
    ]


# YouTube Web CLient
client = InnerTube("WEB", "2.20240105.01.00")

# ShortCircuit - Dell just DESTROYED the Surface Pro! - Dell XPS 13 2-in-1
video = client.next("BV1O7RR-VoA")

engagement_panels = extract_engagement_panels(video)
comments = engagement_panels[ENGAGEMENT_SECTION_COMMENTS]
comments_header = comments["header"]["engagementPanelTitleHeaderRenderer"]
comments_title = parse_text(comments_header["title"])
comments_context = parse_text(comments_header["contextualInfo"])
comments_menu_items = parse_sort_filter_sub_menu(comments_header["menu"])
comments_top = comments_menu_items[C0MMENTS_TOP]
comments_top_continuation = comments_top["serviceEndpoint"]["continuationCommand"][
    "token"
]

print(f"{comments_title} ({comments_context})...")
print()

comments_continuation = client.next(continuation=comments_top_continuation)

comments = extract_comments(comments_continuation)

for comment in comments:
    comment_renderer = comment["comment"]["commentRenderer"]

    comment_author = comment_renderer["authorText"]["simpleText"]
    comment_content = parse_text(comment_renderer["contentText"])

    print(f"[{comment_author}]")
    print(comment_content)
    print()
