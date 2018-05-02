# coding=utf-8
from unittest import TestCase
from main import utils

class TestNormalize_data(TestCase):
    def test_normalize_data(self):
        nm = utils.normalize_data('あｱa')
        expect = 'あアa'
        self.assertEqual(nm, expect)


class TestGet_hashval(TestCase):
    def test_get_hashval(self):
        hs = utils.get_hashval('', '')
        expect = 'a69f73cca23a9ac5c8b567dc185a756e97c982164fe25859e0d1dcc1475c80a615b2123af1f5f94c11e3e9402c3ac558f500199d95b6d3e301758586281dcd26'.upper()
        self.assertEqual(hs, expect)
