import pytest
import os

import pycanlii.Enumerations
from pycanlii.canlii import CanLII

@pytest.fixture
def config():
    try:
        return {
            'key': os.environ['CANLII_URL'],
        }
    except KeyError as err:
        raise Exception('You must set the environment variable {}'.format(err.args[0]))

@pytest.fixture
def canlii(config):
    return CanLII(config['key'], pycanlii.Enumerations.Language.en)

