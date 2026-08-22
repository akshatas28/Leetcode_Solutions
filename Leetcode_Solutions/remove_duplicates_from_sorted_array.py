# leetcode: problem 26 : array

# remove duplicates from sorted array

# input nums= [ 1,1,2 ]

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        expectedNums =[]
        count=0
        for i in range(len(nums)):
            if nums[i] in expectedNums:
                count+=1
            else: 
                expectedNums.append(nums[i])
            if i == len(nums)-1:
                expectedNums.extend(["_"] * count)
        nums[:] = expectedNums
        k=len(nums)-count
        return k