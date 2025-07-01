from innertube.locale import Location, Language, Locale


def test_location() -> None:
    location: Location = Location.ALGERIA

    assert location.country_code == "DZ"
    assert location.country_name == "Algeria"
    assert str(location) == "DZ"
    assert Location.from_code("DZ") == location
    assert Location.from_code("invalid") is None


def test_language() -> None:
    language: Language = Language.AZERBAIJANI

    assert language.language_code == "az"
    assert language.language_name == "Azerbaijani"
    assert language.language_name_native == "Azərbaycan"
    assert str(language) == "az"
    assert Language.from_code("az") == language
    assert Language.from_code("invalid") is None


def test_locale() -> None:
    locale: Locale = Locale("en", "GB")

    assert locale.language == "en"
    assert locale.location == "GB"
    assert locale.accept_language() == "en,GB"
