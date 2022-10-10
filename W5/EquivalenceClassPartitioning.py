import unittest
import shop


class EquivalenceClassPartitioning(unittest.TestCase):

    def test1(self):
        args = (-10, 10)
        self.assertEqual(shop.get_product_reviews(*args), "Invalid in")

    def test2(self):
        args = (20, 10)
        self.assertEqual(shop.get_product_reviews(*args), "b, 1")

    def test3(self):
        args = (70, 10)
        self.assertEqual(shop.get_product_reviews(*args), "a, 1")

    def test4(self):
        args = (2000, 10)
        self.assertEqual(shop.get_product_reviews(*args), "Invalid in")

    def test5(self):
        args = (10, -10)
        self.assertEqual(shop.get_product_reviews(*args), "Invalid in")

    def test6(self):
        args = (10, 10)
        self.assertEqual(shop.get_product_reviews(*args), "b, 1")

    def test7(self):
        args = (10, 50)
        self.assertEqual(shop.get_product_reviews(*args), "b, 2")

    def test8(self):
        args = (10, 75)
        self.assertEqual(shop.get_product_reviews(*args), "b, 3")

    def test9(self):
        args = (10, 110)
        self.assertEqual(shop.get_product_reviews(*args), "Invalid in")


if __name__ == '__main__':
    unittest.main()
