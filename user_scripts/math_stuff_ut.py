import unittest
from user_scripts import cross_sum


class TestMathFunctions(unittest.TestCase):
    def test_cross_sum_positive(self):
        testdata = 56785
        expected_result = 31
        print "SQ: Unit Test executed - test_cross_sum_positive"
        self.assertEqual(cross_sum(testdata), expected_result)

    def test_cross_sum_negative(self):
        testdata = -431
        expected_result = False
        print "SQ: Unit Test executed - test_cross_sum_negative"
        self.assertEqual(cross_sum(testdata), expected_result)


if __name__ == '__main__':
    unittest.main()
