import pycanlii.pycanliibase as base
import os

class LegislationDatabase(base.PyCanliiBase):

    def __init__(self, apikey, language="en"):
        base.PyCanliiBase.__init__(self, apikey, language)


if __name__ == '__main__':
    x = LegislationDatabase(os.environ["CANLII_KEY"])