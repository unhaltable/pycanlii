import pytest
import os

import pycanlii.enumerations
from pycanlii.canlii import CanLII
from pycanlii.case import Case
from pycanlii.legislation import Legislation

@pytest.fixture
def config():
    try:
        return {
            'key': os.environ['CANLII_KEY'],
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

@pytest.fixture
def legis_en(config):
    data = {
      "databaseId": "car",
      "legislationId": "sor-86-946",
      "title": "Abatement of Duties Payable Regulations",
      "citation": "SOR/86-946",
      "type": "REGULATION"
    }
    return Legislation(data, config['key'], pycanlii.enumerations.Language.en)

@pytest.fixture
def legis_fr(config):
    data = {
      "databaseId": "car",
      "legislationId": "dors-96-383",
      "title": "Décret sur l\u0027abandon et la poursuite des procédures, 1996",
      "citation": "DORS/96-383",
      "type": "REGULATION"
    }
    return Legislation(data, config['key'], pycanlii.enumerations.Language.fr)