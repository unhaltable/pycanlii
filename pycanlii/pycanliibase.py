import requests

class PyCanliiBase(object):

    def __init__(self, apikey, language):
        self._key = apikey
        self._lang = language

    def _request(self, url, authenticated, *url_variables, **query_parameters):
        """
        Sends a request to the input url, with the url parameters
        place in order with a / between each and with the
        query parameters input

        :param url:
        :param authenticated: A boolean representing if this request
        should be authenticated or not
        :param url_variables:
        :param query_parameters:
        :return:
        """
        if authenticated:
            query_parameters['api_key'] = self._key

        url += "/" + self._lang.name
        for var in url_variables:
            url += "/" + var

        result = None
        if len(query_parameters):
            result = requests.get(url, params=query_parameters)
        else:
            result = requests.get(url)

        if result.status_code == requests.codes.ok:
            return result
        else:
            raise Exception("Status code not okay, responded with response code " + str(result.status_code))