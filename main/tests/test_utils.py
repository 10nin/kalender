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
        expect = 'A69F73CCA23A9AC5C8B567DC185A756E97C982164FE25859E0D1DCC1475C80A615B2123AF1F5F94C11E3E9402C3AC558F500199D95B6D3E301758586281DCD26'
        self.assertEqual(hs, expect)


class TestGet_unique_str(TestCase):
    def test_get_unique_str(self):
        res = utils.get_unique_str(10)
        self.assertEqual(len(res), 10)
