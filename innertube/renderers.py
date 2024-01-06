from typing import Any, Mapping, MutableMapping, Optional, Sequence, TypeVar, Union
from typing_extensions import Annotated, TypeAlias

import humps
import pydantic
import rich

from .raw_enums import ButtonStyle, IconType

from . import utils


def build_abs_key(field: Union[str, int], parent: Optional[str]) -> str:
    sep: str = "." if isinstance(field, str) else ""

    if isinstance(field, int):
        field = f"[{field}]"

    if parent is None:
        return field

    return f"{parent}{sep}{field}"


DataMap: TypeAlias = Mapping[str, Mapping[str, Any]]
DataSeq: TypeAlias = Sequence[DataMap]
Data: TypeAlias = Union[DataMap, DataSeq]


def parse_renderable(data: Data, /, *, parent: Optional[str] = None):
    assert utils.is_renderable(data)

    if isinstance(data, Sequence):
        return [
            parse_renderable(item, parent=build_abs_key(index, parent))
            for index, item in enumerate(data)
        ]

    key = next(iter(data))
    value = data[key]

    abs_key: str = build_abs_key(key, parent)

    if key not in RENDERERS:
        raise Exception(f"No renderer available for {key!r} ({abs_key})")

    render_cls: type = RENDERERS[key]

    rich.print(f"{abs_key} -> render({key!r}, {set(value.keys())})")

    return render_cls.model_validate(value)


Renderable = Annotated[Any, pydantic.BeforeValidator(parse_renderable)]


C = TypeVar("C", bound=type)

RENDERERS: MutableMapping[str, type] = {}


def renderer(cls: C) -> C:
    renderer_id: str = humps.camelize(cls.__name__) + "Renderer"

    RENDERERS[renderer_id] = cls

    return cls


class BaseModel(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        extra="forbid",
        alias_generator=humps.camelize,
    )


class ComplexTextRun(BaseModel):
    text: str


class ComplexText(BaseModel):
    runs: Sequence[ComplexTextRun]

    # def join(self) -> str:
    #     return "".join(run for run in self.runs)


class SimpleText(BaseModel):
    simple_text: str


Text: TypeAlias = Union[ComplexText, SimpleText]


class AccessibilityData(BaseModel):
    label: str


class Accessibility(BaseModel):
    accessibility_data: AccessibilityData


class BrowseEndpoint(BaseModel):
    browse_id: str


class Icon(BaseModel):
    icon_type: IconType


class SignInEndpoint(BaseModel):
    hack: bool


class NavigationEndpoint(BaseModel):
    click_tracking_params: str
    browse_endpoint: Optional[BrowseEndpoint] = None
    sign_in_endpoint: Optional[SignInEndpoint] = None


@renderer
class Button(BaseModel):
    style: ButtonStyle
    is_disabled: bool
    text: SimpleText
    navigation_endpoint: NavigationEndpoint
    tracking_params: str


@renderer
class SingleColumnBrowseResultsRenderer:
    pass


@renderer
class SingleColumnBrowseResultsRenderer:
    pass


@renderer
class MusicImmersiveHeaderRenderer:
    pass


@renderer
class GuideEntry(BaseModel):
    navigation_endpoint: NavigationEndpoint
    icon: Icon
    tracking_params: str
    formatted_title: ComplexText
    accessibility: Accessibility
    is_primary: bool


@renderer
class GuideSection(BaseModel):
    tracking_params: str
    items: Sequence[Renderable]


@renderer
class GuideSigninPromo(BaseModel):
    action_text: ComplexText
    descriptiveText: ComplexText
    signInButton: Renderable
