import pycanlii.Enumerations as enums

class TestEnums(object):

    #This probably seems redundant, it's just to check if it works on all versions
    def test_enums(self):
        assert enums.LegislationJurisdiction.ca == enums.LegislationJurisdiction.ca
