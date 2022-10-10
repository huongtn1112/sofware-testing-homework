import unittest
import shop


class BoundaryValueAnalysis(unittest.TestCase):

    def test1(self):
        args = (0, 50)
        self.assertEqual(shop.get_product_reviews(*args), "b, 2")

    def test2(self):
        args = (1, 50)
        self.assertEqual(shop.get_product_reviews(*args), "b, 2")

    def test3(self):
        args = (1000, 50)
        self.assertEqual(shop.get_product_reviews(*args), "a, 2")

    def test4(self):
        args = (999, 50)
        self.assertEqual(shop.get_product_reviews(*args), "a, 2")

    def test5(self):
        args = (500, 50)
        self.assertEqual(shop.get_product_reviews(*args), "a, 2")

    def test6(self):
        args = (500, 0)
        self.assertEqual(shop.get_product_reviews(*args), "a, 1")

    def test7(self):
        args = (500, 1)
        self.assertEqual(shop.get_product_reviews(*args), "a, 1")

    def test8(self):
        args = (500, 100)
        self.assertEqual(shop.get_product_reviews(*args), "a, 3")

    def test9(self):
        args = (500, 99)
        self.assertEqual(shop.get_product_reviews(*args), "a, 3")


if __name__ == '__main__':
    unittest.main()
