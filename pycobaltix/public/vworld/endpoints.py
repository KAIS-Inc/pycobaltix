import math
import os

import httpx

from pycobaltix.public.vworld.response.buldSnList import BuildingInfo
from pycobaltix.public.vworld.response_format import ResponseFormat
from pycobaltix.schemas.responses import PaginatedAPIResponse, PaginationInfo


class VWorldAPI:
    def __init__(self, api_key: str | None = None, domain: str | None = None):
        self.api_key = api_key or os.getenv("VWORLD_API_KEY")
        self.domain = domain or os.getenv("VWORLD_DOMAIN")
        if not self.api_key:
            raise ValueError("VWORLD_API_KEY 환경 변수가 설정되지 않았습니다")
        if not self.domain:
            raise ValueError("VWORLD_DOMAIN 환경 변수가 설정되지 않았습니다")
        self.base_url = "https://api.vworld.kr"

    def _make_get_request(self, endpoint: str, **params):
        """공통 요청 메서드"""
        # 모든 요청에 key, domain 자동 추가
        params.update({"key": self.api_key, "domain": self.domain})
        params.update({"format": ResponseFormat.JSON.value})

        # None 값 제거
        filtered_params = {k: v for k, v in params.items() if v is not None and v != ""}

        url = f"{self.base_url}{endpoint}"
        response = httpx.get(url, params=filtered_params)
        response.raise_for_status()
        return response.json()

    def buldSnList(
        self,
        pnu: str,
        agbldgSn: str | None = None,
        numOfRows: int = 100,
        pageNo: int = 1,
    ):
        """건물일련번호조회"""
        response = self._make_get_request(
            "/ned/data/buldSnList",
            pnu=pnu,
            agbldgSn=agbldgSn,
            numOfRows=numOfRows,
            pageNo=pageNo,
        )
        if "ldaregVOList" not in response:
            return PaginatedAPIResponse(
                data=[],
                pagination=PaginationInfo(
                    currentPage=1,
                    totalPages=1,
                    totalCount=0,
                    count=0,
                    hasNext=False,
                    hasPrevious=False,
                ),
            )
        total_count = int(response["ldaregVOList"]["totalCount"])
        total_pages = math.ceil(total_count / numOfRows)
        current_page = int(response["ldaregVOList"]["pageNo"])

        pagination = PaginationInfo(
            currentPage=current_page,
            totalPages=total_pages,
            totalCount=total_count,
            count=numOfRows,
            hasNext=current_page < total_pages,
            hasPrevious=current_page > 1,
        )

        return PaginatedAPIResponse(
            success=True,
            message="success",
            status=200,
            data=[
                BuildingInfo.from_dict(item)
                for item in response["ldaregVOList"]["ldaregVOList"]
            ],
            pagination=pagination,
        )

    def buldHoCoList(
        self,
        pnu: str,
        agbldgSn: str | None = None,
        buldDongNm: str | None = None,
        buldFloorNm: str | None = None,
        buldHoNm: str | None = None,
        numOfRows: int = 100,
        pageNo: int = 1,
    ):
        """건물호수조회"""
        response = self._make_get_request(
            "/ned/data/buldHoCoList",
            pnu=pnu,
            agbldgSn=agbldgSn,
            buldDongNm=buldDongNm,
            buldFloorNm=buldFloorNm,
            buldHoNm=buldHoNm,
            numOfRows=numOfRows,
            pageNo=pageNo,
        )
        if "ldaregVOList" not in response:
            return PaginatedAPIResponse(
                data=[],
                pagination=PaginationInfo(
                    currentPage=1,
                    totalPages=1,
                    totalCount=0,
                    count=0,
                    hasNext=False,
                    hasPrevious=False,
                ),
            )

        total_count = int(response["ldaregVOList"]["totalCount"])
        total_pages = math.ceil(total_count / numOfRows)
        current_page = int(response["ldaregVOList"]["pageNo"])

        pagination = PaginationInfo(
            currentPage=current_page,
            totalPages=total_pages,
            totalCount=total_count,
            count=numOfRows,
            hasNext=current_page < total_pages,
            hasPrevious=current_page > 1,
        )

        return PaginatedAPIResponse(
            data=[
                BuildingInfo.from_dict(item)
                for item in response["ldaregVOList"]["ldaregVOList"]
            ],
            pagination=pagination,
        )
