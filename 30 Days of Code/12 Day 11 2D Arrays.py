import math
import os
import random
import re
import sys


def hourGlass(arr):
    
    temp = []
    for i in range(0, 4):
        for j in range(0, 4):
            s = sum(arr[i][j:j+3])+arr[i+1][j+1]+sum(arr[i+2][j:j+3])
            temp.append(s)
    
    return max(temp)

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(hourGlass(arr))