# -*- coding: utf-8 -*-
import pytest
import os

import pycanlii.enums
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
    return CanLII(config['key'], pycanlii.enums.Language.en)

@pytest.fixture
def case_fr():
    return {
        'databaseId': 'qccs',
        'caseId': { 'fr' : '2008qccs3554' },
        'title' : u'Société 3505 Ste-Famille inc. c. Régie du logement',
        'citation' : '2008 QCCS 3554 (CanLII)'
    }

@pytest.fixture
def case_en():
    return {
        'databaseId': 'csc-scc',
        'caseId': { 'en' : '2011scc47' },
        'title' : 'Crookes v. Newton',
        'citation' : '[2011] 3 SCR 269, 2011 SCC 47 (CanLII)'
    }

@pytest.fixture
def case(case_en, config):
    return Case(case_en, config['key'])

@pytest.fixture
def legis_en():
    return {
      "databaseId": "car",
      "legislationId": "sor-86-946",
      "title": "Abatement of Duties Payable Regulations",
      "citation": "SOR/86-946",
      "type": "REGULATION"
    }

@pytest.fixture
def legis_fr():
    return {
      "databaseId": "car",
      "legislationId": "dors-96-383",
      "title": "Décret sur l\u0027abandon et la poursuite des procédures, 1996",
      "citation": "DORS/96-383",
      "type": "REGULATION"
    }

@pytest.fixture
def legislation(legis_en, config):
    return Legislation(legis_en, config['key'], pycanlii.enums.Language.en)

