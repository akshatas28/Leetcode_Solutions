# leetcode 50 : pow(x,n)

x=2.00000
n=10
#1024.00000

import math

def calculate_power(x, n):
    total = math.pow(x, n)
    return float(f"{total:.5f}")


#else

return round(math.pow(x, n), 5)