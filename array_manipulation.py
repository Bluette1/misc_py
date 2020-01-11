#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    m = len(queries)
    arr = [0] * n

    max_val = 0

    starts = [0] * n

    ends = [0] * n

    summands = []

    for query in range(m):
        starts[queries[query][1]] += queries[query][2]
        ends[queries[query][1]] += queries[query][2]


    for i in range(n):
        start = starts[i]
            arr[i] += queries[2]
            max_val = max(max_val, arr[i])
    return (max_val)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
