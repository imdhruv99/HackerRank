import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    
    sock_pairs = 0
    colors = dict()
    
    ar.sort()
    ar.append('#')
    
    i = 0
    while i < n:
        
        if ar[i] == ar[i+1]:
            
            sock_pairs = sock_pairs + 1
            
            i += 2
        
        else:
            
            i += 1
            
    return sock_pairs
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
