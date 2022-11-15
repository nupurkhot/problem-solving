#!/bin/python3

import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    level = 0
    count = 0
    inthevalley = False
    for i in range(len(path)):
        if path[i]=="U":
            level += 1 
        else:
            level -= 1
        #print(path[i], level)
        if level < 0:
            inthevalley = True
        if level == 0 and inthevalley:
            count+=1
            inthevalley = False
    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    steps = int(input().strip())
    path = input()
    result = countingValleys(steps, path)
    fptr.write(str(result) + '\n')
    fptr.close()
