import pycanlii.pycanliibase as base
import pycanlii.enums as enums
import requests
from bs4 import BeautifulSoup

class LegislationDatabase(base.PyCanliiBase):
    """
    A database of CanLII Legislation. This object is both indexable and iterable.
    """

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
        self._citation = None
        self._dateScheme = None
        self._startDate = None
        self._endDate = None
        self._repealed = None

        # Used to store the content of the Legislation
        self._content = None

        if (data['type'] == "REGULATION"):
            self.type = enums.LegislationType.Regulation
        elif (data['type'] == "STATUTE"):
            self.type = enums.LegislationType.Statute
        else:
            # cause of the API this should never actually happen
            raise Exception("Invalid legislation type")


    def _populate(self):
        if not self._populated:
            legis = self._request("http://api.canlii.org/v1/legislationBrowse", True, self.databaseId, self.legislationId)
            legis = legis.json()
            self._url = legis['url']
            self._dateScheme = enums.DateScheme[legis['dateScheme']]
            self._startDate = legis['startDate']
            self._endDate = legis['endDate']
        
            if (legis['repealed']  == 'NO'):
                self._repealed = False
            else:
                self._repealed = True

            self._populated = True

    @property
    def content(self):
        """
        Returns the HTML content of the legislation

        :return: Returns a BeautifulSoup object representing the HTML content of the legislation
        """

        self._populate()

        if not self._content:
            req = requests.get(self._url)
            self._content = BeautifulSoup(req.content)

        return self._content

    @property
    def url(self):
        """
        Gets the string representation of the URL where this legislation is located

        :return: A string representing the URL where this legislation is located
        """
        self._populate()
        return self._url

    @property
    def citation(self):
        """
        Gets the string representation of the citation of this legislation object

        :return: A string representing the citation of this legislation object
        """
        self._populate()
        return self._citation

    @property
    def dateScheme(self):
        self._populate()
        return self._dateScheme

    @property
    def startDate(self):
        self._populate()
        return self._startDate

    @property
    def endDate(self):
        self._populate()
        return self._endDate

    @property
    def repealed(self):
        self._populate()
        return self._repealed


