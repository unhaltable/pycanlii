__author__ = 'jonathanwebb'

import pycanlii.pycanliibase as base
import pycanlii.legislation
import pycanlii.case
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
            self._db.append(pycanlii.legislation.LegislationDatabase(db, self.key, self.lang))

        return self._db


    def case_databases(self):
        l = self._request("http://api.canlii.org/v1/caseBrowse", True)
        casedb = []
        dbs = l.json()['caseDatabases']
        for db in dbs:
            casedb.append(pycanlii.case.CaseDatabase(db, self.key, self.lang))

        return casedb

    #NYI
    def search(self, fullText, resultCount=100, offset=0):
        '''
        Returns upto the first 100 results of a search in CanLII. If you can potentially return more than 100 results
        you're bad and you should feel bad. Put in a more precise search.
        :param fullText: Your search query
        :param resultCount: Some number less than 100. Okay?
        :param offset: This can technically be anything, any positive integer anyways. I'd be wary of going
        _too_ hard on this one
        :return: A list of results
        '''
        results = self._request("http://api.canlii.org/v1/search", True, fullText=fullText,
                                 resultCount=resultCount, offset=offset).json()
        results = results['results']
        l = []
        for result in results:
            if 'legislation' in result:
                l.append(pycanlii.legislation.Legislation(result['legislation'], self.key, self.lang))
            else:
                l.append(pycanlii.case.Case(result['case'], self.key, self.lang))
        return l


if __name__ == '__main__':
    x = CanLII(os.environ["CANLII_KEY"])
    #y = x.request("http://api.canlii.org/v1/legislationBrowse", True)
    #print(y.json())
    y = x.search("employment")
    print(y)
