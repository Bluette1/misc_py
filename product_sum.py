import math
from functools import reduce
from itertools import combinations_with_replacement

def find_factors(num):
    """
    This will count factors of a given number
    :param num:
    :return factors: An array containing factors of the given number
    """
    result_list = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            if i == math.sqrt(num):
                result_list += [i]
            else:
                result_list += [i, num // i]
    return result_list


def min_product_sum(n):
    """
    A brute force version for calculating minimum product sums with poor running for large values
    of n. See details at https://projecteuler.net/problem=88
    :param n: the number of elements in a set of minimum product sums
    :return: minimum product sum
    """
    # Initialise array to hold min product_sums from 2...n
    product_sums = [0] * (n - 1)
    set_count = 1  # tracker for the number of min product_sums found
    natural_num = 1 # Set the first natural number
    while (set_count < n):
        factors = find_factors(natural_num)
        i = 2
        # while i < n + 1 and n <= natural_num:
        for i in range(2, n + 1):
            min = -1
            # Both of these long-winded approaches work
            combinations = combinations_with_replacement(factors, i)
            # combinations = combinations_with_replacement(list(range(1, natural_num + 1)), i)
            for tuple in combinations:
                total = sum(list(tuple))
                product = reduce(lambda x, y: x * y, tuple)
                if total == product:
                    # print(tuple)
                    # print(product)
                    if min > total or min == -1:
                        min = total
            if min != -1 and product_sums[i - 2] == 0:
                product_sums[i - 2] = min
                set_count += 1
            # i += 1
        natural_num += 1

    return sum(set(product_sums))


# def main():
#     print(*min_product_sum(6))
#     print(set(min_product_sum(6)))
#     print(list(set(min_product_sum(6))))
#     print(sum(list(set(min_product_sum(6)))))

# Call to main function to run the program
# if __name__ == "__main__":
#     main()


# print(*combinations_with_replacement(find_factors(4), 2))
# combinations = combinations_with_replacement(find_factors(4), 2)
# product_sums = set()
# set_count = 0
# for tuple in combinations:
#     list_tuple = list(tuple)
#     total = sum(list(tuple))
#     product = reduce(lambda x, y: x * y, tuple)
#     # product = numpy.prod(tuple)
#     if total == product:
#         print(tuple)
#         product_sums.add(sum)
#         set_count += 1

