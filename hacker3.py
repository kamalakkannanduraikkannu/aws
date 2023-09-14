#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    n=s.split(" ")
    k=""
    for i in n:
     if (i.isdigit()):
       k+=i+" "
     else:
       k+=i.capitalize()+" "
    print(k)
if __name__ == '__main__':