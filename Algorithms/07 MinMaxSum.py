#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    
    for i in range(0, len(arr)):
        arr[i] = int(arr[i])
    
    s = sum(arr)
    print(str(s-max(arr)) + " " + str(s - min(arr)))
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)