class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = 0
        for i in range(1, n + 1):
            if n % i == 0:
                total += nums[i - 1] * nums[i - 1]
        return total

class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return sum(x * x for i, x in enumerate(nums, 1) if n % i == 0)
        
        