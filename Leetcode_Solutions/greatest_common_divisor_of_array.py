# leetcode : problem 1979 : find greatest common divisor or array

import math 
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return math.gcd((min(nums)),(max(nums)))