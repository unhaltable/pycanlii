import pycanlii.pycanliibase as base
import pycanlii.enumerations as enums
import pycanlii.helpers
import os

class LegislationDatabase(base.PyCanliiBase):

    def __init__(self, data, apikey, language=enums.Language.en):
        base.PyCanliiBase.__init__(self, apikey, language)
        self.name = data['name']

        if (data['type'] == "REGULATION"):
            self.type = enums.LegislationType.Regulation
        elif (data['type'] == "STATUTE"):
            self.type = enums.LegislationType.Statute
        else:
            #cause of the API this should never actually happen
            raise Exception("Invalid legislation type")

        self.id = data["databaseId"]
        #still need to add jurisdiction although for basic functionality, strictly speaking, not required
        self.jurisdiction = pycanlii.helpers.getJurisdiction(data['jurisdiction'])
        self.legislation = []
        self._populated = False

    #nyi
    def _getLegislation(self):
        legis = self._request("http://api.canlii.org/v1/legislationBrowse", False, self.id)

    def __iter__(self):
        if not self._populated:
            self._getLegislation()
            self._populated = True
        return self.legislation.__iter__()

    def __getitem__(self, item):
        if not self._populated:
            self._getLegislation()
            self._populated = True
        return self.legislation[item]

class Legislation(base.PyCanliiBase):

    def __init__(self, apikey, language=enums.Language.en, **data):
        base.PyCanliiBase.__init__(self, apikey, language)



if __name__ == '__main__':
    x = LegislationDatabase(os.environ["CANLII_KEY"])