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


class TestValid_date(TestCase):
    def test_valid_date(self):
        correct_date = ['201805', '099901', '199910', '200007', '211912', '203903']
        invalid_date = ['', '-12345', '201813', '200000', 'ABCDEF', '038038']
        for c in correct_date:
            self.assertTrue(utils.valid_date(c))
        for i in invalid_date:
            self.assertFalse(utils.valid_date(i))


class TestSplit_request_date(TestCase):
    def test_split_request_date(self):
        request_date = '201805'
        correct_year = 2018
        correct_month = 5
        self.assertEqual(utils.split_request_date(request_date)[0], correct_year)
        self.assertEqual(utils.split_request_date(request_date)[1], correct_month)


class TestGet_prev_and_next_month(TestCase):
    def test_get_prev_and_next_month(self):
        year1 = 2018
        month1 = 5
        prev1 = '201804'
        next1 = '201806'
        ret = utils.get_prev_and_next_month(year1, month1)
        self.assertEqual(ret[0], prev1)
        self.assertEqual(ret[1], next1)

        year2 = 2018
        month2 = 12
        prev2 = '201811'
        next2 = '201901'
        ret = utils.get_prev_and_next_month(year2, month2)
        self.assertEqual(ret[0], prev2)
        self.assertEqual(ret[1], next2)

        year3 = 2018
        month3 = 1
        prev3 = '201712'
        next3 = '201802'
        ret = utils.get_prev_and_next_month(year3, month3)
        self.assertEqual(ret[0], prev3)
        self.assertEqual(ret[1], next3)

