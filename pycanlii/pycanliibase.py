import requests
import datetime

class PyCanliiBase(object):
    """
    The base object in the pycanlii library. All objects in the library inherit from it.
    """

    def __init__(self, apikey, language):
        self._key = apikey
        self._lang = language

    def _request(self, url, authenticated, *url_variables, **query_parameters):
        """
        Sends a request to the input url, with the url parameters
        place in order with a / between each and with the
        query parameters input.

        :param url: A url with where to send the request
        :param authenticated: A boolean representing if this request
        should be authenticated or not
        :param url_variables:
        :param query_parameters:
        :return: A response object
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

        result.raise_for_status()
        return result

    def _getDate(self, daystr):
        """
        Accepts a string of the form "YYYY-MM-DD" and returns a date object representing that date, if daystr is the
        empty string, None is returned.

        :param daystr: A string in the format "YYYY-MM-DD" representing a date
        :return: A date object determined by the input string
        """
        if daystr == "":
            return None
        else:
            return datetime.date(int(daystr[0:4]), int(daystr[5:7]), int(daystr[8:10]))