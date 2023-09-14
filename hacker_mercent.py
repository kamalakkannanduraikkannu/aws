import math
import os
import random
import re
import sys
def sockMerchant(n, ar):
    # Write your code here
    pears = 0
    color = set()
    for i in range(len(ar)):
        if ar[i] not in color:
            color.add(ar[i])
        else:
         pears += 1
         color.remove(ar[i])
    return pears

if __name__ == '__main__':
  

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
    
