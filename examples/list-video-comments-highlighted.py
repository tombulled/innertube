from innertube import InnerTube

# YouTube Web CLient
CLIENT = InnerTube("WEB", "2.20240105.01.00")


def parse_text(text):
    return "".join(run["text"] for run in text["runs"])


def flatten(items):
    flat_items = {}

    for item in items:
        key = next(iter(item))
        val = item[key]

        flat_items.setdefault(key, []).append(val)

    return flat_items


def flatten_item_sections(item_sections):
    return {
        item_section["sectionIdentifier"]: item_section
        for item_section in item_sections
    }


def extract_comments(next_continuation_data):
    return [
        continuation_item["commentThreadRenderer"]
        for continuation_item in next_continuation_data["onResponseReceivedEndpoints"][
            1
        ]["reloadContinuationItemsCommand"]["continuationItems"][:-1]
    ]


def extract_comments_continuation_token(next_data):
    contents = flatten(
        next_data["contents"]["twoColumnWatchNextResults"]["results"]["results"][
            "contents"
        ]
    )
    item_sections = flatten_item_sections(contents["itemSectionRenderer"])
    comment_item_section_content = item_sections["comment-item-section"]["contents"][0]
    comments_continuation_token = comment_item_section_content[
        "continuationItemRenderer"
    ]["continuationEndpoint"]["continuationCommand"]["token"]

    return comments_continuation_token


def get_comments(video_id, params=None):
    video = CLIENT.next(video_id, params=params)

    continuation_token = extract_comments_continuation_token(video)

    comments_continuation = CLIENT.next(continuation=continuation_token)

    return extract_comments(comments_continuation)


def print_comment(comment):
    comment_renderer = comment["comment"]["commentRenderer"]

    comment_author = comment_renderer["authorText"]["simpleText"]
    comment_content = parse_text(comment_renderer["contentText"])

    print(f"[{comment_author}]")
    print(comment_content)
    print()


video_id = "BV1O7RR-VoA"

# Get comments for a given video
comments = get_comments(video_id)

# Select a comment to highlight (in this case the 3rd one)
comment = comments[2]

# Print the comment we're going to highlight
print("### Highlighting Comment: ###")
print()
print_comment(comment)
print("---------------------")
print()

# Extract the 'params' to highlight this comment
params = comment["comment"]["commentRenderer"]["publishedTimeText"]["runs"][0][
    "navigationEndpoint"
]["watchEndpoint"]["params"]

# Get comments, but highlighting the selected comment
highlighted_comments = get_comments(video_id, params=params)

print("### Comments: ###")
print()

for comment in highlighted_comments:
    print_comment(comment)
