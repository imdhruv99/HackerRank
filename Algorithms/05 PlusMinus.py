#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    
    negative = []
    positive = []
    zero = []
    
    for i in range(len(arr)):
        
        if arr[i] < 0:
            negative.append(arr[i])
            continue
        
        elif arr[i] > 0:
            positive.append(arr[i])
            continue
        
        else:
            zero.append(arr[i])
    
    ratioOfPositiveNumber = len(positive) / len(arr)
    ratioOfNegativeNumber = len(negative) / len(arr)
    ratioOfZero = len(zero) / len(arr)
    
    print(ratioOfPositiveNumber)
    print(ratioOfNegativeNumber)
    print(ratioOfZero)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
