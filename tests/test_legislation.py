from pycanlii.legislation import Legislation
from pycanlii.enumerations import Language, LegislationType
from bs4 import BeautifulSoup

class TestLegislation:

    def test__init__(self, legis_en, legis_fr, config):
        en = Legislation(legis_en, config['key'], Language.en)
        fr = Legislation(legis_fr, config['key'], Language.fr)

        assert en.databaseId == legis_en['databaseId']
        assert en.legislationId == legis_en['legislationId']
        assert en.title == legis_en['title']
        assert en.citation == legis_en['citation']
        assert en.type == LegislationType[legis_en['type'].capitalize()]
        assert en._key == config['key']
        assert en._lang == Language.en

        assert fr.databaseId == legis_fr['databaseId']
        assert fr.legislationId == legis_fr['legislationId']
        assert fr.title == legis_fr['title']
        assert fr.citation == legis_fr['citation']
        assert fr.type == LegislationType[legis_fr['type'].capitalize()]
        assert fr._key == config['key']
        assert fr._lang == Language.fr

    def test_getContent(self, legislation):
        assert type(legislation.getContent()) == BeautifulSoup

    def test__iter__(self, canlii):
        db = canlii.legislation_databases()
        for legis in db:
            pass

    def test__getitem__(self, canlii):
        db = canlii.legislation_databases()
        db[5]
        db[11000]