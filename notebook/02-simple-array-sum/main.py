#!/bin/python3
#
# HackerRank folio
# solved by Michael Gene Brockus
#
import os
import sys

#
# Should add the values from the array to
# the summary and return the value of sum.
#
# arg-list:
#   -> ar: array of integers
#
def simpleArraySum(ar):
    count = 0
    for it in ar:
        count += it
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
