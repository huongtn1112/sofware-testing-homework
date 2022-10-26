import unittest

import shop


class DataFlowTesting(unittest.TestCase):
    def test1(self):
        args = (500, 10)
        self.assertEqual(shop.get_product_reviews(*args), "a, 1")

    def test2(self):
        args = (-10, -10)
        self.assertEqual(shop.get_product_reviews(*args), "Invalid in")

    def test3(self):
        args = (10, 10)
        self.assertEqual(shop.get_product_reviews(*args), "b, 1")

    def test4(self):
        args = (500, 50)
        self.assertEqual(shop.get_product_reviews(*args), "a, 2")

    def test5(self):
        args = (500, 80)
        self.assertEqual(shop.get_product_reviews(*args), "a, 3")

if __name__ == '__main__':
    unittest.main()
