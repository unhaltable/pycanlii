import pycanlii.enumerations as enums


def getJurisdiction(location_code):
    """
    Takes a 2 character string that represents the jurisdiction that some CanLII document to associated with and returns
    an enumeration value that represents it
    :param location_code: A 2 character string of the postal code route for some province or territory in Canada
    :return: An enumeration representing the jurisdiction of the postal code
    """

    return enums.LegislationJurisdiction.__members__[location_code]
