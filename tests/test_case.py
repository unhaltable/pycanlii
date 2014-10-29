from bs4 import BeautifulSoup
from pycanlii.case import Case
from pycanlii.enumerations import Language


class TestCase:

    def test__init__(self, case_en, case_fr, config):
        en = Case(case_en, config['key'])
        fr = Case(case_fr, config['key'])

        assert en.databaseId == case_en['databaseId']
        assert en.caseId == case_en['caseId']
        assert en.title == case_en['title']
        assert en.citation == case_en['citation']
        assert en._key == config['key']
        assert en._lang == Language.en

        assert fr.databaseId == case_fr['databaseId']
        assert fr.caseId == case_fr['caseId']
        assert fr.title == case_fr['title']
        assert fr.citation == case_fr['citation']
        assert fr._key == config['key']
        assert fr._lang == Language.fr