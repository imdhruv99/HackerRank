import math
import os
import random
import re
import sys

def migratoryBirds(arr):
    
    count = [0 for i in range(5)]
    
    for i in arr:
        
        count[i-1] += 1
    
    max_count = max(count)
    
    for i in range(5):
        
        if count[i] == max_count:
    
            return i + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
