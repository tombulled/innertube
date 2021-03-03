import enum

class Language(enum.Enum):
    EnglishUK = 'en-GB'
    EnglishUS = 'en-US'
    French    = 'fr'

class Location(enum.Enum):
    UnitedKingdom = 'GB'
    UnitedStates  = 'US'
    France        = 'FR'
