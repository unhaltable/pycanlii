import pycanlii.pycanliibase as base
import pycanlii.enumerations as enums
import pycanlii.helpers
from pycanlii.canlii import *
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
        legis = self._request("http://api.canlii.org/v1/legislationBrowse", True, self.id).json()['legislations']
        for legislation in legis:
            self.legislation.append(Legislation(legislation, self.key, self.lang))


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

    def __init__(self, data, apikey, language=enums.Language.en):
        base.PyCanliiBase.__init__(self, apikey, language)
        self.databaseId = data['databaseId']
        self.legislationId = data['legislationId']
        self.title = data['title']
        self.citation = data['citation']

        self.populated = False
        self.url = ''






        if (data['type'] == "REGULATION"):
            self.type = enums.LegislationType.Regulation
        elif (data['type'] == "STATUTE"):
            self.type = enums.LegislationType.Statute
        else:
            #cause of the API this should never actually happen
            raise Exception("Invalid legislation type")


    def _populate(self):
        legis = self._request("http://api.canlii.org/v1/legislationBrowse", True, self.databaseId, self.legislationId)
        legis = legis.json()




if __name__ == '__main__':
    canlii = CanLII(os.environ["CANLII_KEY"])
    legislation = canlii.legislation_databases()