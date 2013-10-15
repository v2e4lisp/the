import unittest
from helper import the


class TestTheMagic(unittest.TestCase):
    def setUp(self):
        self.true = self.assertTrue
        self.false = self.assertFalse
        self.r = self.assertRaises

    def test_eq(self):
        self.true(the(1) == 1)
        with self.r(Exception):
            the("a") == "x"

    def test_gt(self):
        self.true(the(1) > 0)
        with self.r(Exception):
            the(1) > 1

    def test_lt(self):
        self.true(the(1) < 2)
        with self.r(Exception):
            the(1) < 0

    def test_ge(self):
        self.true(the(2) >= 2)
        self.true(the(3) >= 2)
        with self.r(Exception):
            the(1) >= 2

    def test_le(self):
        self.true(the(1) <= 1)
        self.true(the(1) <= 2)
        with self.r(Exception):
            the(1) <= 0

    def test_ne(self):
        self.true(the(1) != 2)
        with self.r(Exception):
            the(1) != 1

    def test_contains(self):
        self.true(the(1) in range(1, 3))
        with self.r(Exception):
            the(1) in range(2, 10)

    def test_getitem(self):
        d = {"a": 1, "b": 2, "c": 3}
        self.true(the(d)["a"] == 1)
        with self.r(Exception):
            the(d)["a"] == 2

    def test_iter(self):
        for i in the(range(1, 4)):
            i > 0
        with self.r(Exception):
            for i in the(range(1, 4)):
                i > 1

if __name__ == '__main__':
    unittest.main()