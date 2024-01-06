from enum import Enum, auto


class StrEnum(str, Enum):
    pass


class ButtonStyle(StrEnum):
    STYLE_DEFAULT: str = "STYLE_DEFAULT"


# A "service" as listed under "responseContext.serviceTrackingParams"
class Service(StrEnum):
    CSI: str = "CSI"
    GFEEDBACK: str = "GFEEDBACK"
    ECATCHER: str = "ECATCHER"


# E.g., {"icon": {"iconType": "TAB_HOME"}}
class IconType(StrEnum):
    LIBRARY_MUSIC = "LIBRARY_MUSIC"
    TAB_EXPLORE = "TAB_EXPLORE"
    TAB_HOME = "TAB_HOME"


class SharePanelType(Enum):
    SHARE_PANEL_TYPE_UNIFIED_SHARE_PANEL = auto()
