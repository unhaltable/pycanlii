import pycanlii.pycanliibase as base
import pycanlii.enums as enums
import requests
from bs4 import BeautifulSoup

class LegislationDatabase(base.PyCanliiBase):
    """
    A database of CanLII Legislation. This object is both indexable and iterable.

    Attributes:
        :name: A string representing the name of this LegislationDatabase
        :type: An instance of the LegislationType enum indicating what kind of Legislation this LegislationDatabasecontains
        :id: A string representing the databaseId of this LegislationDatabase
        :jurisdiction: An instance of a Jurisdiction enum representing the Jurisdiction of the Legislation in this
        LegislationDatabase
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
            raise Exception("Invalid legislation type, this should never happen, please open an issue on our " +
                            "git repo at https://github.com/sherlocke/pycanlii and include your stack trace " +
                            "or alternatively contribute and submit a pull request :)")

        self.id = data["databaseId"]
        # still need to add jurisdiction although for basic functionality, strictly speaking, not required
        self.jurisdiction = enums.Jurisdiction[data['jurisdiction']]
        self._legislation = []
        self._populated = False

    def _getLegislation(self):
        legis = self._request("http://api.canlii.org/v1/legislationBrowse", True, self.id).json()['legislations']
        for legislation in legis:
            self._legislation.append(Legislation(legislation, self._key, self._lang))

    def __iter__(self):
        if not self._populated:
            self._getLegislation()
            self._populated = True
        return self._legislation.__iter__()

    def __getitem__(self, item):
        if not self._populated:
            self._getLegislation()
            self._populated = True
        return self._legislation[item]


class Legislation(base.PyCanliiBase):
    """
    An object representing Legislation on CanLII

    Attributes:
        :databaseId: A string representing the databaseId of this legislation
        :legislationId: A string representing the legislationId of this legislation
        :title: A string representing the title of this legislation
        :content: A BeautifulSoup object representing the HTML content of this legislation
        :url: A string representing the URL where this legislation can be found
        :dateScheme: An instance of the DateScheme enum representing the dateScheme of this legislation
        :startDate: A date object representing the start date of this legislation
        :endDate: A date object representing the end date of this legislation. If it has no end date yet, it will be none
        :repealed: A boolean representing whether or not this legislation has been repealed or not
    """

    def __init__(self, data, apikey, language=enums.Language.en):
        base.PyCanliiBase.__init__(self, apikey, language)
        self.databaseId = data['databaseId']
        self.legislationId = data['legislationId']
        self.title = data['title']
        self._citation = data['citation']

        self._populated = False
        self._url = None
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
            self._startDate = self._getDate(legis['startDate'])
            self._endDate = self._getDate(legis['endDate'])
        
            if (legis['repealed']  == 'NO'):
                self._repealed = False
            else:
                self._repealed = True

            self._populated = True

    @property
    def content(self):
        if not self._content:
            req = requests.get(self.url)
            self._content = BeautifulSoup(req.content)

        return self._content

    @property
    def url(self):
        self._populate()
        return self._url

    @property
    def citation(self):
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


