__author__ = 'jonathanwebb'

import pycanlii.pycanliibase as base
from pycanlii.legislation import LegislationDatabase
from pycanlii.case import CaseDatabase
import os
import pycanlii.Enumerations as enums

class CanLII(base.PyCanliiBase):

    def __init__(self, apikey, language=enums.Language.en):
        base.PyCanliiBase.__init__(self, apikey, language)
        self._db = None

    def legislation_databases(self):
        '''
        Returns a list of LegislationDatabase objects, each representing a legislation database on CanLII
        :return: A list of LegislationDatabase objects
        '''
        l = self._request("http://api.canlii.org/v1/legislationBrowse", True)
        self._db = []
        dbs = l.json()['legislationDatabases']
        for db in dbs:
            self._db.append(LegislationDatabase(db, self.key, self.lang))

        return self._db


    def case_databases(self):
        l = self._request("http://api.canlii.org/v1/caseBrowse", True)
        casedb = []
        dbs = l.json()['caseDatabases']
        for db in dbs:
            casedb.append(CaseDatabase(db, self.key, self.lang))

        return casedb


if __name__ == '__main__':
    x = CanLII(os.environ["CANLII_KEY"])
    #y = x.request("http://api.canlii.org/v1/legislationBrowse", True)
    #print(y.json())
    y = x.legislation_databases()
    print(y)