__author__ = 'jonathanwebb'

import pycanlii.pycanliibase as base
from pycanlii.legislation import LegislationDatabase
import os

class CanLII(base.PyCanliiBase):

    def __init__(self, apikey, language="en"):
        base.PyCanliiBase.__init__(self, apikey, language)

    def legislation_databases(self):
        l = self.request("http://api.canlii.org/v1/legislationBrowse", True)
        ret = []
        dbs = l.json()['legislationDatabases']
        for db in dbs:
            ret.append(LegislationDatabase(db, self.key, self.lang))

        return ret


if __name__ == '__main__':
    x = CanLII(os.environ["CANLII_KEY"])
    #y = x.request("http://api.canlii.org/v1/legislationBrowse", True)
    #print(y.json())
    y = x.legislation_databases()
    print(y)