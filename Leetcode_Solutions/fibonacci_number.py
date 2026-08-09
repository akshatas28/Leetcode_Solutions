# leetcode

# 509. Fibonacci Number

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        n1=0
        n2=1
        i=2
        if n == 0 or n==1:
            return n
        while i<=n:
            n1, n2 = n2, n1 + n2
            i+=1
        return (n2)