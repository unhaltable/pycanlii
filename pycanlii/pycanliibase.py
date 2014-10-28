import requests
import json
import os

class PyCanliiBase(object):

    def __init__(self, apikey, language):
        self.key = apikey
        self.lang = language


    def _request(self, url, authenticated, *url_variables, **query_parameters):
        '''
        Sends a request to the input url, with the url parameters
        place in order with a / between each and with the
        query parameters input
        :param url:
        :param authenticated: A boolean representing if this request
        should be authenticated or not
        :param url_variables:
        :param query_parameters:
        :return:
        '''
        if authenticated:
            query_parameters['api_key'] = self.key

        url += "/" + self.lang.name
        for var in url_variables:
            url += "/" + var

        if (len(query_parameters)):
            return requests.get(url, params=query_parameters)
        else:
            return requests.get(url)

if __name__ == '__main__':
    x = PyCanliiBase(os.environ["CANLII_KEY"])
    #y = x.request("http://api.canlii.org/v1/legislationBrowse", True)
    #print(y.json())
    y = x._request("http://api.canlii.org/v1/legislationBrowse", True)
    print(y.json()['legislationDatabases'])