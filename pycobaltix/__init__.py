"""
pycobaltix - API 응답 형식을 정의하는 유틸리티 패키지
"""

__version__ = "0.1.0"

from pycobaltix.schemas.responses import (
    APIResponse,
    PaginatedAPIResponse,
    PaginationInfo,
    ErrorResponse,
)

from pycobaltix.slack import SlackWebHook, SlackBot

__all__ = [
    "APIResponse",
    "PaginatedAPIResponse",
    "PaginationInfo",
    "ErrorResponse",
    "SlackWebHook",
    "SlackBot",
]