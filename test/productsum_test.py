import unittest
from random import randint
import src as productsum


MAX_N = 12000
productsum = productsum.min_product_sum


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_basic_tests(self):
        self.assertEqual(productsum(2), 4, 'productsum(%d)' % 2)
        self.assertEqual(productsum(3), 10, 'productsum(%d)' % 3)
        self.assertEqual(productsum(6), 30, 'productsum(%d)' % 6)
        self.assertEqual(productsum(10), 61, 'productsum(%d)' % 10)
        self.assertEqual(productsum(12), 61, 'productsum(%d)' % 12)

        # The reference solution should be placed here, in order to prevent the warrior from abusing your reference solution

    def _productsum(self, kmax):

        def prodsum(p, s, c, start):
            k = p - s + c  # product - sum + number of factors
            if k < kmax:
                if p < n[k]: n[k] = p
                for i in range(start, kmax // p * 2 + 1):
                    prodsum(p * i, s + i, c + 1, i)

        kmax += 1
        n = [2 * kmax] * kmax
        prodsum(1, 1, 1, 2)

        return sum(set(n[2:]))
        # When running a random test, you need to make sure that the expected value is computed first.
        # If the warrior's solution is run first, it may mutate the input list and thus easily bypass them.
        # Also, take extra care on your own reference solution to not mutate the input :)


    def _do_one_test(self):
        # n = randint(2, MAX_N)
        n = 4
        print("nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn::::::::::::::::::::", n)
        expected = self._productsum(n)
        self.assertEqual(productsum(n), expected, 'productsum(%d)' % n)
        # test.assert_equals(two_oldest_ages(ages), _reference(ages))

        # The number of random tests must be enough to test every possible aspects of the input.
        # The rule of thumb is 100 tests, but you have to think carefully according to the requirements of your Kata.

    print('Random Test Cases')
    def test_random_cases(self):
        for _ in range(2):
            self._do_one_test()


if __name__ == '__main__':
    # unittest.main()
    unittest.main(verbosity=2)
