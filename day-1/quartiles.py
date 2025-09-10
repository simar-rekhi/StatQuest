#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    arr1 = sorted(arr)
    n = len(arr1)
    mid = n // 2

    def compute_median(test_arr):
        m = len(test_arr)
        if m % 2 == 0:
            return (test_arr[m//2 - 1] + test_arr[m//2]) // 2
        else:
            return test_arr[m//2]

    q2 = compute_median(arr1)

    if n % 2 == 0:
        lower = arr1[:mid]
        upper = arr1[mid:]
    else:
        lower = arr1[:mid]
        upper = arr1[mid+1:]

    q1 = compute_median(lower)
    q3 = compute_median(upper)

    return [q1, q2, q3]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
