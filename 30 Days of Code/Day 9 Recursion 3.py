import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    return n if n == 1 else factorial(n - 1) * n

print(factorial(int(input())))