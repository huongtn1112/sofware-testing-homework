import unittest

import shop


class ControlFlowTest(unittest.TestCase):
    def test(self):
        args = (-10, 10)
        self.assertEqual(shop.get_product_reviews(*args), "Invalid in")

    def test1(self):
        args = (70, 10)
        self.assertEqual(shop.get_product_reviews(*args), "a, 1")

    def test2(self):
        args = (70, 60)
        self.assertEqual(shop.get_product_reviews(*args), "a, 2")

    def test3(self):
        args = (70, 90)
        self.assertEqual(shop.get_product_reviews(*args), "a, 3")

    def test4(self):
        args = (20, 10)
        self.assertEqual(shop.get_product_reviews(*args), "b, 1")

    def test5(self):
        args = (20, 60)
        self.assertEqual(shop.get_product_reviews(*args), "b, 2")

    def test6(self):
        args = (20, 90)
        self.assertEqual(shop.get_product_reviews(*args), "b, 3")


if __name__ == '__main__':
    unittest.main()
