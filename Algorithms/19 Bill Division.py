import math
import os
import random
import re
import sys


def bonAppetit(bill, k, b):
    
    billed = b - (sum(bill) - bill[k]) // 2
    
    if billed:
        
        print(billed)
    
    else:
        
        print("Bon Appetit")

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
