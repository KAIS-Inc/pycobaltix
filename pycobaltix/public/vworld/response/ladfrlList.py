class LandInfo:
    def __init__(
        self,
        pnu: str,
        ldCodeNm: str,
        ldCode: str,
        mnnmSlno: str,
        regstrSeCode: str,
        regstrSeCodeNm: str,
        lndcgrCode: str,
        lndcgrCodeNm: str,
        lndpclAr: str,
        posesnSeCode: str,
        posesnSeCodeNm: str,
        cnrsPsnCo: str,
        ladFrtlSc: str,
        ladFrtlScNm: str,
        lastUpdtDt: str,
    ):
        self.pnu = pnu
        self.ldCodeNm = ldCodeNm
        self.ldCode = ldCode
        self.mnnmSlno = mnnmSlno
        self.regstrSeCode = regstrSeCode
        self.regstrSeCodeNm = regstrSeCodeNm
        self.lndcgrCode = lndcgrCode
        self.lndcgrCodeNm = lndcgrCodeNm
        self.lndpclAr = lndpclAr
        self.posesnSeCode = posesnSeCode
        self.posesnSeCodeNm = posesnSeCodeNm
        self.cnrsPsnCo = cnrsPsnCo
        self.ladFrtlSc = ladFrtlSc
        self.ladFrtlScNm = ladFrtlScNm
        self.lastUpdtDt = lastUpdtDt

    def to_dict(self):
        return {
            "pnu": self.pnu,
            "ldCodeNm": self.ldCodeNm,
            "ldCode": self.ldCode,
            "mnnmSlno": self.mnnmSlno,
            "regstrSeCode": self.regstrSeCode,
            "regstrSeCodeNm": self.regstrSeCodeNm,
            "lndcgrCode": self.lndcgrCode,
            "lndcgrCodeNm": self.lndcgrCodeNm,
            "lndpclAr": self.lndpclAr,
            "posesnSeCode": self.posesnSeCode,
            "posesnSeCodeNm": self.posesnSeCodeNm,
            "cnrsPsnCo": self.cnrsPsnCo,
            "ladFrtlSc": self.ladFrtlSc,
            "ladFrtlScNm": self.ladFrtlScNm,
            "lastUpdtDt": self.lastUpdtDt,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "LandInfo":
        return cls(
            pnu=data["pnu"],
            ldCodeNm=data["ldCodeNm"],
            ldCode=data["ldCode"],
            mnnmSlno=data["mnnmSlno"],
            regstrSeCode=data["regstrSeCode"],
            regstrSeCodeNm=data["regstrSeCodeNm"],
            lndcgrCode=data["lndcgrCode"],
            lndcgrCodeNm=data["lndcgrCodeNm"],
            lndpclAr=data["lndpclAr"],
            posesnSeCode=data["posesnSeCode"],
            posesnSeCodeNm=data["posesnSeCodeNm"],
            cnrsPsnCo=data["cnrsPsnCo"],
            ladFrtlSc=data["ladFrtlSc"],
            ladFrtlScNm=data["ladFrtlScNm"],
            lastUpdtDt=data["lastUpdtDt"],
        )
