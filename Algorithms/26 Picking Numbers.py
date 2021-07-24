import math
import os
import random
import re
import sys


def pickingNumbers(a):
    
    sortedA = sorted(a)
    result = 1
    current = 1
    diff = 0
    
    for i in range(1, len(sortedA)):
        
        diff += sortedA[i] - sortedA[i - 1]
        
        if diff > 1:
            result = max(result, current)
            current = 1
            diff = 0
        else:
            current += 1
    result = max(result, current)
    
    return result
    
if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
