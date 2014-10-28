import pycanlii.Enumerations as enums

class TestEnums(object):

    #This probably seems redundant, it's just to check if it works on all versions of python
    def test_enums(self):
        #Tests if the enum will run at all
        assert enums.LegislationJurisdiction.ca == enums.LegislationJurisdiction.ca

        #Tests if you can get the name of the enum
        assert enums.Language.en == 'en'

        #Tests if the __members__ variable exists
        assert enums.DateScheme.__members__['DOWNLOAD_DATE'] == enums.DateScheme.DOWNLOAD_DATE