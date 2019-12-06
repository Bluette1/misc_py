from random import randint
from src import min_product_sum as productsum
import test_framework as test

MAX_N = 12000


@test.describe('Fixed Tests')
def fixed_tests():
    # Basic Tests: Test the basic behavior (basic understanding of the task).
    @test.it('Basic Test Cases')
    def basic_tests():
        test.assert_equals(productsum(3), 10, 'productsum(%d)' % 3)
        test.assert_equals(productsum(6), 30, 'productsum(%d)' % 6)
        test.assert_equals(productsum(12), 61, 'productsum(%d)' % 12)

    # Edge Cases: Test the edge cases, which are not common but hard to correctly solve.
    # These are needed because "rare but hard cases" are not well-covered by random tests only.
    @test.it('Edge Cases')
    def edge_case_tests():
        test.assert_equals(productsum(2), 4, 'productsum(%d)' % 2)


# Random tests: Test the behavior against your reference solution.
# This is mainly to prevent the warrior passing the tests by hardcoding the fixed cases.
# The functions `random`, `randint`, `choice`, `shuffle`, and `sample` inside Python's `random` module will be helpful.
@test.describe('Random Tests')
def random_tests():
    # The reference solution should be placed here, in order to prevent the warrior from abusing your reference solution
    def _productsum(kmax):
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
    def _do_one_test():
        n = randint(2, MAX_N)
        expected = _productsum(n)
        test.assert_equals(productsum(n), expected, 'productsum(%d)' % n)
        # test.assert_equals(two_oldest_ages(ages), _reference(ages))

    # The number of random tests must be enough to test every possible aspects of the input.
    # The rule of thumb is 100 tests, but you have to think carefully according to the requirements of your Kata.
    @test.it('Random Test Cases')
    @test.timeout(10)
    def random_test_cases():
        for _ in range(50):
            _do_one_test()