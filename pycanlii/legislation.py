import pycanlii.pycanliibase as base
import pycanlii.enumerations as enums
import os

class LegislationDatabase(base.PyCanliiBase):

    def __init__(self, data, apikey, language="en"):
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
        self.jurisdiction = ""
        self.legislation = []

    #nyi
    def _getLegislation(self):
        legis = self.request("http://api.canlii.org/v1/legislationBrowse", False, self.id)

class Legislation(base.PyCanliiBase):

    def __init__(self, apikey, language="en"):
        base.PyCanliiBase.__init__(self, apikey, language)


if __name__ == '__main__':
    x = LegislationDatabase(os.environ["CANLII_KEY"])