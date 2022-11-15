#!/bin/python3

import math
import os
import random
import re
import sys

def makeAnagram(a, b):
    a_set = set(a)
    b_set = set(b)
    c = a_set | b_set
    count = 0
    for alpha in c:
        diff = abs(a.count(alpha)-b.count(alpha))
        count+=diff
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = input()
    b = input()
    res = makeAnagram(a, b)
    fptr.write(str(res) + '\n')
    fptr.close()
