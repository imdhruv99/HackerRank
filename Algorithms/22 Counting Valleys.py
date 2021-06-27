import math
import os
import random
import re
import sys


def countingValleys(steps, path):
    
    seaLevel = 0	
    valley = 0
    
    for i in range(steps):
        
        if path[i] == 'U':
            
            seaLevel += 1
            
            if seaLevel == 0:
                
                valley += 1
                
        else:
            
            seaLevel -= 1
    
    return valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
