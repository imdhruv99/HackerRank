import math
import os
import random
import re
import sys

def catAndMouse(x, y, z):
    
    CatA = abs(x-z)
    CatB = abs(y-z)
    
    if CatA == CatB:
        return "Mouse C"
    elif CatA > CatB:
        return "Cat B"
    else:
        return "Cat A"
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
