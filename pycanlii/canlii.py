__author__ = 'jonathanwebb'

import pycanlii.pycanliibase as base

class CanLII(base.PyCanliiBase):

    def __init__(self, apikey, language="en"):
        base.PyCanliiBase.__init__(self, apikey, language)