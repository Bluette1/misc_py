#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(queue):
    track = [0] * len(queue)

    for posn in range(len(queue)):
        track[posn] = posn + 1

    minBribes = 0

    valid = True
    for posn in range(len(queue)):

        if queue[posn] != track[posn]:

            if queue[posn] > posn + 1:
                skip = queue[posn] - (posn + 1)
            else:
                idx = findIndex(queue[posn], posn + 1, track)

                skip = idx - posn

            if skip > 2:  # invalid move
                valid = False
                break
            else:
                # perform the move
                shift(queue[posn], track, posn, skip)
                minBribes += skip

    if not valid:
        print("Too chaotic")
    #
    else:
        print(minBribes)


# Method to perform the shift
def shift(skip, track, idx, moves):
    temp = track[idx]
    track[idx] = skip
    for i in range(moves):
        if idx + 1 < len(track):
            store = track[idx + 1]
            track[idx + 1] = temp
            temp = store
        else:
            track[idx + 1] = temp

        idx += 1


# Method to search for a given number in the arr and return its index
def findIndex(num, start, arr):
    for idx in range(start, len(arr)):
        if arr[idx] == num:
            return idx
    return -1


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        # n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
