import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    n = len(arr)
    d1 = 0
    d2 = 0
    for i in range(0, n):
        for j in range(0, n):
            
            if i == j:
                d1 += arr[i][j]
            
            if i == n - j - 1:
                d2 += arr[i][j]
    
    return abs(d1 - d2)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
