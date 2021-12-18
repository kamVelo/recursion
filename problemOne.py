"""
Given a positive integer n:
create a recursive function which returns the sum of all non-negative integers up to and including n
"""
import sys
def sumToN(n:int):
    if n == 1: return 1
    else:
        return n + sumToN(n-1)

if __name__ == '__main__':
    print(sumToN(10))