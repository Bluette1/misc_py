#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
# See https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
def hourglassSum(arr):
    max_hourglass = -100

    for i in range(4):
        for j in range(4):
            hourglass_sum = find_sum_hourglass(i, j, arr)
            if hourglass_sum > max_hourglass:
                max_hourglass = hourglass_sum
    return max_hourglass


def find_sum_hourglass(i, j, arr):
    sum_first_row = 0
    for k in range(j, j + 3):
        sum_first_row += arr[i][k]

    mid = arr[i + 1][j + 1]

    sum_third_row = 0
    for k in range(j, j + 3):
        sum_third_row += arr[i + 2][k]
    return sum_first_row + mid + sum_third_row


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
