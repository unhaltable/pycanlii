from enum import Enum

class PyCanLiiEnum(Enum):

    def getMember(self, name):
        '''
        Takes the name of a member of the enum and returns the member
        :param name: A string representing the name of a member of the enum
        :return: A member of the enum represented by the string
        '''
        return self.__members__[name]

class LegislationType(PyCanLiiEnum):
    Regulation = 0
    Statute = 1

class LegislationJurisdiction(PyCanLiiEnum):
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

class Language(PyCanLiiEnum):
    fr = 0
    en = 1 # because english is greater than french

class DateScheme(PyCanLiiEnum):
    ENTRY_INTO_FORCE = 0
    DOWNLOAD_DATE = 1
