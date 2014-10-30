import pytest
import os

import pycanlii.enumerations
from pycanlii.canlii import CanLII
from pycanlii.case import Case

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
    return CanLII(config['key'], pycanlii.enumerations.Language.en)

@pytest.fixture
def case_fr(config):
    data = {
        'databaseId': 'qccs',
        'caseId': { 'fr' : '2008qccs3554' },
        'title' : 'Société 3505 Ste-Famille inc. c. Régie du logement',
        'citation' : '2008 QCCS 3554 (CanLII)'
    }
    return Case(data, config['key'], pycanlii.enumerations.Language.en)

@pytest.fixture
def case_en(config):
    data = {
        'databaseId': 'csc-scc',
        'caseId': { 'en' : '2008scc9' },
        'title' : 'Dunsmuir v. New Brunswick',
        'citation' : '[2008] 1 SCR 190, 2008 SCC 9 (CanLII)'
    }
    return Case(data, config['key'], pycanlii.enumerations.Language.en)