from enum import Enum

class LegislationType(Enum):
    Regulation = 0
    Statute = 1

class LegislationJurisdiction(Enum):
    ca = 0
    ab = 1
    mb = 2
    nb = 3
    nl = 4
    ns = 5
    nt = 6
    nu = 7
    on = 8
    pe = 9
    qc = 10
    sk = 11
    yk = 12
    bc = 13

class Language(Enum):
    fr = 0
    en = 1 # because english is greater than french

class DataScheme(Enum):
    ENTRY_INTO_FORCE = 0
    DOWNLOAD_DATE = 1
