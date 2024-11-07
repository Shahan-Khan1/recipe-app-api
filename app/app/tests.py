from django.test import SimpleTestCase
from . import calc


class Add_test(SimpleTestCase):

    # test addition
    def test_add_fun(self):
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    # test subtraction
    def test_sub_fun(self):
        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)
