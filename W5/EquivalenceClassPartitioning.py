import unittest
import shop


class EquivalenceClassPartitioning(unittest.TestCase):

    def test(self):
        args = (50, 5000)
        self.assertEqual(shop.get_product_reviews(*args), "a, 2")


if __name__ == '__main__':
    unittest.main()
