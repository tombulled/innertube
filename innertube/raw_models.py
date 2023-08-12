import pydantic
import humps
from typing import Optional, Sequence

from .raw_enums import SharePanelType


class BaseModel(pydantic.BaseModel):
    class Config:
        alias_generator = humps.camelize


class ServiceTrackingParam(BaseModel):
    key: str
    value: str


class ServiceTrackingParams(BaseModel):
    service: str
    params: Sequence[ServiceTrackingParam]


class MainAppWebResponseContext(BaseModel):
    logged_out: bool
    tracking_param: str


class WebResponseContextExtensionData(BaseModel):
    has_decorated: bool


class ResponseContext(BaseModel):
    visitor_data: str
    service_tracking_params: Sequence[ServiceTrackingParams]
    max_age_seconds: int
    main_app_web_response_context: Optional[MainAppWebResponseContext] = None
    web_response_context_extension_data: Optional[
        WebResponseContextExtensionData
    ] = None


class Response(BaseModel):
    response_context: ResponseContext


class ShareEntityEndpoint(BaseModel):
    serialized_share_entity: str
    share_panel_type: SharePanelType
