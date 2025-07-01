from dataclasses import dataclass
from enum import Enum
from typing import Optional, Union

__all__ = ("Location", "Language", "Locale")


class Location(Enum):
    """ISO 3166-1 alpha-2 Country Code"""

    country_code: str
    country_name: str

    def __init__(self, code: str, name: str) -> None:
        self.country_code = code
        self.country_name = name

    def __str__(self) -> str:
        return self.country_code

    @classmethod
    def from_code(cls, country_code: str, /) -> Optional["Location"]:
        location: Location
        for location in cls:
            if location.country_code.lower() == country_code.lower():
                return location

        return None

    ALGERIA = ("DZ", "Algeria")
    ARGENTINA = ("AR", "Argentina")
    AUSTRALIA = ("AU", "Australia")
    AUSTRIA = ("AT", "Austria")
    AZERBAIJAN = ("AZ", "Azerbaijan")
    BAHRAIN = ("BH", "Bahrain")
    BANGLADESH = ("BD", "Bangladesh")
    BELARUS = ("BY", "Belarus")
    BELGIUM = ("BE", "Belgium")
    BOLIVIA = ("BO", "Bolivia")
    BOSNIA_AND_HERZEGOVINA = ("BA", "Bosnia and Herzegovina")
    BRAZIL = ("BR", "Brazil")
    BULGARIA = ("BG", "Bulgaria")
    CAMBODIA = ("KH", "Cambodia")
    CANADA = ("CA", "Canada")
    CHILE = ("CL", "Chile")
    COLOMBIA = ("CO", "Colombia")
    COSTA_RICA = ("CR", "Costa Rica")
    CROATIA = ("HR", "Croatia")
    CYPRUS = ("CY", "Cyprus")
    CZECHIA = ("CZ", "Czechia")
    DENMARK = ("DK", "Denmark")
    DOMINICAN_REPUBLIC = ("DO", "Dominican Republic")
    ECUADOR = ("EC", "Ecuador")
    EGYPT = ("EG", "Egypt")
    EL_SALVADOR = ("SV", "El Salvador")
    ESTONIA = ("EE", "Estonia")
    FINLAND = ("FI", "Finland")
    FRANCE = ("FR", "France")
    GEORGIA = ("GE", "Georgia")
    GERMANY = ("DE", "Germany")
    GHANA = ("GH", "Ghana")
    GREECE = ("GR", "Greece")
    GUATEMALA = ("GT", "Guatemala")
    HONDURAS = ("HN", "Honduras")
    HONG_KONG = ("HK", "Hong Kong")
    HUNGARY = ("HU", "Hungary")
    ICELAND = ("IS", "Iceland")
    INDIA = ("IN", "India")
    INDONESIA = ("ID", "Indonesia")
    IRAQ = ("IQ", "Iraq")
    IRELAND = ("IE", "Ireland")
    ISRAEL = ("IL", "Israel")
    ITALY = ("IT", "Italy")
    JAMAICA = ("JM", "Jamaica")
    JAPAN = ("JP", "Japan")
    JORDAN = ("JO", "Jordan")
    KAZAKHSTAN = ("KZ", "Kazakhstan")
    KENYA = ("KE", "Kenya")
    KUWAIT = ("KW", "Kuwait")
    LAOS = ("LA", "Laos")
    LATVIA = ("LV", "Latvia")
    LEBANON = ("LB", "Lebanon")
    LIBYA = ("LY", "Libya")
    LIECHTENSTEIN = ("LI", "Liechtenstein")
    LITHUANIA = ("LT", "Lithuania")
    LUXEMBOURG = ("LU", "Luxembourg")
    MALAYSIA = ("MY", "Malaysia")
    MALTA = ("MT", "Malta")
    MEXICO = ("MX", "Mexico")
    MOLDOVA = ("MD", "Moldova")
    MONTENEGRO = ("ME", "Montenegro")
    MOROCCO = ("MA", "Morocco")
    NEPAL = ("NP", "Nepal")
    NETHERLANDS = ("NL", "Netherlands")
    NEW_ZEALAND = ("NZ", "New Zealand")
    NICARAGUA = ("NI", "Nicaragua")
    NIGERIA = ("NG", "Nigeria")
    NORTH_MACEDONIA = ("MK", "North Macedonia")
    NORWAY = ("NO", "Norway")
    OMAN = ("OM", "Oman")
    PAKISTAN = ("PK", "Pakistan")
    PANAMA = ("PA", "Panama")
    PAPUA_NEW_GUINEA = ("PG", "Papua New Guinea")
    PARAGUAY = ("PY", "Paraguay")
    PERU = ("PE", "Peru")
    PHILIPPINES = ("PH", "Philippines")
    POLAND = ("PL", "Poland")
    PORTUGAL = ("PT", "Portugal")
    PUERTO_RICO = ("PR", "Puerto Rico")
    QATAR = ("QA", "Qatar")
    ROMANIA = ("RO", "Romania")
    RUSSIA = ("RU", "Russia")
    SAUDI_ARABIA = ("SA", "Saudi Arabia")
    SENEGAL = ("SN", "Senegal")
    SERBIA = ("RS", "Serbia")
    SINGAPORE = ("SG", "Singapore")
    SLOVAKIA = ("SK", "Slovakia")
    SLOVENIA = ("SI", "Slovenia")
    SOUTH_AFRICA = ("ZA", "South Africa")
    SOUTH_KOREA = ("KR", "South Korea")
    SPAIN = ("ES", "Spain")
    SRI_LANKA = ("LK", "Sri Lanka")
    SWEDEN = ("SE", "Sweden")
    SWITZERLAND = ("CH", "Switzerland")
    TAIWAN = ("TW", "Taiwan")
    TANZANIA = ("TZ", "Tanzania")
    THAILAND = ("TH", "Thailand")
    TUNISIA = ("TN", "Tunisia")
    TURKEY = ("TR", "Turkey")
    UGANDA = ("UG", "Uganda")
    UKRAINE = ("UA", "Ukraine")
    UNITED_ARAB_EMIRATES = ("AE", "United Arab Emirates")
    UNITED_KINGDOM = ("GB", "United Kingdom")
    UNITED_STATES = ("US", "United States")
    URUGUAY = ("UY", "Uruguay")
    VENEZUELA = ("VE", "Venezuela")
    VIETNAM = ("VN", "Vietnam")
    YEMEN = ("YE", "Yemen")
    ZIMBABWE = ("ZW", "Zimbabwe")


class Language(Enum):
    """IETF BCP-47 Language"""

    language_code: str
    language_name: str
    language_name_native: str

    def __init__(
        self, language_code: str, language_name: str, language_name_native: str
    ) -> None:
        self.language_code = language_code
        self.language_name = language_name
        self.language_name_native = language_name_native

    def __str__(self) -> str:
        return self.language_code

    @classmethod
    def from_code(cls, language_code: str, /) -> Optional["Language"]:
        language: Language
        for language in cls:
            if language.language_code.lower() == language_code.lower():
                return language

        return None

    AFRIKAANS = ("af", "Afrikaans", "Afrikaans")
    AZERBAIJANI = ("az", "Azerbaijani", "Azərbaycan")
    INDONESIAN = ("id", "Indonesian", "Bahasa Indonesia")
    MALAY = ("ms", "Malay", "Bahasa Malaysia")
    BOSNIAN = ("bs", "Bosnian", "Bosanski")
    CATALAN = ("ca", "Catalan", "Català")
    CZECH = ("cs", "Czech", "Čeština")
    DANISH = ("da", "Danish", "Dansk")
    GERMAN = ("de", "German", "Deutsch")
    ESTONIAN = ("et", "Estonian", "Eesti")
    ENGLISH_INDIA = ("en-IN", "English (India)", "English (India)")
    ENGLISH_UK = ("en-GB", "English (UK)", "English (UK)")
    ENGLISH_US = ("en-US", "English (US)", "English (US)")
    SPANISH_SPAIN = ("es", "Spanish (Spain)", "Español (España)")
    SPANISH_LATIN_AMERICA = (
        "es-419",
        "Spanish (Latin America)",
        "Español (Latinoamérica)",
    )
    SPANISH_US = ("es-US", "Spanish (US)", "Español (US)")
    BASQUE = ("eu", "Basque", "Euskara")
    FILIPINO = ("fil", "Filipino", "Filipino")
    FRENCH = ("fr", "French", "Français")
    FRENCH_CANADA = ("fr-CA", "French (Canada)", "Français (Canada)")
    GALICIAN = ("gl", "Galician", "Galego")
    CROATIAN = ("hr", "Croatian", "Hrvatski")
    ZULU = ("zu", "Zulu", "IsiZulu")
    ICELANDIC = ("is", "Icelandic", "Íslenska")
    ITALIAN = ("it", "Italian", "Italiano")
    KISWAHILI = ("sw", "Kiswahili", "Kiswahili")
    LATVIAN = ("lv", "Latvian", "Latviešu valoda")
    LITHUANIAN = ("lt", "Lithuanian", "Lietuvių")
    HUNGARIAN = ("hu", "Hungarian", "Magyar")
    DUTCH = ("nl", "Dutch", "Nederlands")
    NORWEGIAN = ("no", "Norwegian", "Norsk")
    UZBEK = ("uz", "Uzbek", "O‘zbek")
    POLISH = ("pl", "Polish", "Polski")
    PORTUGUESE = ("pt-PT", "Portuguese", "Português")
    PORTUGUESE_BRASIL = ("pt", "Portuguese (Brasil)", "Português (Brasil)")
    ROMANIAN = ("ro", "Romanian", "Română")
    ALBANIAN = ("sq", "Albanian", "Shqip")
    SLOVAK = ("sk", "Slovak", "Slovenčina")
    SLOVENIAN = ("sl", "Slovenian", "Slovenščina")
    SERBIAN = ("sr-Latn", "Serbian", "Srpski")
    FINNISH = ("fi", "Finnish", "Suomi")
    SWEDISH = ("sv", "Swedish", "Svenska")
    VIETNAMESE = ("vi", "Vietnamese", "Tiếng Việt")
    TURKISH = ("tr", "Turkish", "Türkçe")
    BELARUSIAN = ("be", "Belarusian", "Беларуская")
    BULGARIAN = ("bg", "Bulgarian", "Български")
    KYRGYZ = ("ky", "Kyrgyz", "Кыргызча")
    KAZAKH = ("kk", "Kazakh", "Қазақ Тілі")
    MACEDONIAN = ("mk", "Macedonian", "Македонски")
    MONGOLIAN = ("mn", "Mongolian", "Монгол")
    RUSSIAN = ("ru", "Russian", "Русский")
    SERBIAN_CYRILLIC = ("sr", "Serbian (Cyrillic)", "Српски")
    UKRAINIAN = ("uk", "Ukrainian", "Українська")
    GREEK = ("el", "Greek", "Ελληνικά")
    ARMENIAN = ("hy", "Armenian", "Հայերեն")
    HEBREW = ("he", "Hebrew", "עברית")
    URDU = ("ur", "Urdu", "اردو")
    ARABIC = ("ar", "Arabic", "العربية")
    PERSIAN = ("fa", "Persian", "فارسی")
    NEPALI = ("ne", "Nepali", "नेपाली")
    MARATHI = ("mr", "Marathi", "मराठी")
    HINDI = ("hi", "Hindi", "हिन्दी")
    ASSAMESE = ("as", "Assamese", "অসমীয়া")
    BENGALI = ("bn", "Bengali", "বাংলা")
    PUNJABI = ("pa", "Punjabi", "ਪੰਜਾਬੀ")
    GUJARATI = ("gu", "Gujarati", "ગુજરાતી")
    ODIA = ("or", "Odia", "ଓଡ଼ିଆ")
    TAMIL = ("ta", "Tamil", "தமிழ்")
    TELUGU = ("te", "Telugu", "తెలుగు")
    KANNADA = ("kn", "Kannada", "ಕನ್ನಡ")
    MALAYALAM = ("ml", "Malayalam", "മലയാളം")
    SINHALA = ("si", "Sinhala", "සිංහල")
    THAI = ("th", "Thai", "ภาษาไทย")
    LAO = ("lo", "Lao", "ລາວ")
    BURMESE = ("my", "Burmese", "ဗမာ")
    GEORGIAN = ("ka", "Georgian", "ქართული")
    AMHARIC = ("am", "Amharic", "አማርኛ")
    KHMER = ("km", "Khmer", "ខ្មែរ")
    CHINESE_SIMPLIFIED = ("zh-CN", "Chinese (Simplified)", "中文 (简体)")
    CHINESE_TRADITIONAL = ("zh-TW", "Chinese (Traditional)", "中文 (繁體)")
    CHINESE_HONG_KONG = ("zh-HK", "Chinese (Hong Kong)", "中文 (香港)")
    JAPANESE = ("ja", "Japanese", "日本語")
    KOREAN = ("ko", "Korean", "한국어")


@dataclass
class Locale:
    language: str  # HL (Host Language)
    location: Optional[str] = None  # GL (Geographic Location)

    def __init__(
        self, language: Union[str, Language], location: Optional[Union[str, Location]]
    ) -> None:
        if isinstance(language, Language):
            language = language.language_code
        if isinstance(location, Location):
            location = location.country_code

        self.language = language
        self.location = location

    def accept_language(self) -> str:
        return ",".join(
            item for item in (self.language, self.location) if item is not None
        )
