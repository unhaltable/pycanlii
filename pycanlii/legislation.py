import pycanlii.pycanliibase as base
import pycanlii.enumerations as enums
import requests
from bs4 import BeautifulSoup

class LegislationDatabase(base.PyCanliiBase):

    def __init__(self, data, apikey, language=enums.Language.en):
        base.PyCanliiBase.__init__(self, apikey, language)
        self.name = data['name']

        if (data['type'] == "REGULATION"):
            self.type = enums.LegislationType.Regulation
        elif (data['type'] == "STATUTE"):
            self.type = enums.LegislationType.Statute
        else:
            # cause of the API this should never actually happen
            raise Exception("Invalid legislation type")

        self.id = data["databaseId"]
        # still need to add jurisdiction although for basic functionality, strictly speaking, not required
        self.jurisdiction = enums.LegislationJurisdiction[data['jurisdiction']]
        self.legislation = []
        self._populated = False

    def _getLegislation(self):
        legis = self._request("http://api.canlii.org/v1/legislationBrowse", True, self.id).json()['legislations']
        for legislation in legis:
            self.legislation.append(Legislation(legislation, self._key, self._lang))


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

        self._populated = False
        self._url = None
        self._title = None
        self._citation = None
        self._dateScheme = None
        self._startDate = None
        self._endDate = None
        self._repealed = None

        # Used to store the content of the Legislation
        self._content = None

        if (data['type'] == "REGULATION"):
            self.type = enums.LegislationType.Regulation
            self.type = enums.LegislationType.Regulation
        elif (data['type'] == "STATUTE"):
            self.type = enums.LegislationType.Statute
        else:
            # cause of the API this should never actually happen
            raise Exception("Invalid legislation type")


    def _populate(self):
        legis = self._request("http://api.canlii.org/v1/legislationBrowse", True, self.databaseId, self.legislationId)
        legis = legis.json()
        self._url = legis['url']
        self._title = legis['title']
        self._dateScheme = enums.DateScheme[legis['dateScheme']]
        self._startDate = legis['startDate']
        self._endDate = legis['endDate']
        
        if (legis['repealed']  == 'NO'):
            self._repealed = False
        else:
            self._repealed = True

        self._populated = True

    def getContent(self):
        if not self._populated:
            self._populate()

        if not self._content:
            req = requests.get(self._url)
            self._content = BeautifulSoup(req.content)

        return self._content
