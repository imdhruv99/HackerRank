import math
import os
import random
import re
import sys


def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * (tip_percent/100)
    tax = meal_cost * (tax_percent/100)
    totalCost = meal_cost + tip + tax
    print(round(totalCost))
