from bs4 import BeautifulSoup
from pycanlii.case import Case
from pycanlii.legislation import Legislation
from pycanlii.enumerations import Language


class TestCase:

    def test__init__(self, case_en, case_fr, config):
        en = Case(case_en, config['key'])
        fr = Case(case_fr, config['key'])

        assert en.databaseId == case_en['databaseId']
        assert en.caseId == case_en['caseId']['en']
        assert en.title == case_en['title']
        assert en.citation == case_en['citation']
        assert en._key == config['key']
        assert en._lang == Language.en

        assert fr.databaseId == case_fr['databaseId']
        assert fr.caseId == case_fr['caseId']['fr']
        assert fr.title == case_fr['title']
        assert fr.citation == case_fr['citation']
        assert fr._key == config['key']
        assert fr._lang == Language.fr

    def test_getContent(self, case):
        assert type(case.getContent()) == BeautifulSoup

    def test_citedCases(self, case):
        c = case.citedCases()
        if not c == None:
            for i in c:
                assert type(i) == Case

    def test_citingCases(self, case):
        c = case.citingCases()
        if not c == None:
            for i in c:
                assert type(i) == Case

    def test_citedLegislation(self, case):
        c = case.citedLegislation()
        if not c == None:
            for i in c:
                assert type(i) == Legislation
