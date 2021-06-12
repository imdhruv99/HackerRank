import math
import os
import random
import re
import sys

def breakingRecords(scores):
    
    max_ = scores[0]
    min_ = scores[0]
    
    maxCount = 0
    minCount = 0
    
    for i in range(len(scores)):
        
        if scores[i] > max_:
            max_ = scores[i]
            maxCount+=1
            
        if scores[i] < min_:
            min_ = scores[i]
            minCount+=1
            
    return [maxCount, minCount]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()