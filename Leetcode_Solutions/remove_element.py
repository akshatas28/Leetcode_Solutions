# leetcode: problem 27 : array

# remove element

# input nums= [ 3,2,2,3 ]
# val = 3

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        expectedNums =[]
        count=0
        for i in range(len(nums)):
            if nums[i] == val:
                count+=1
            else: 
                expectedNums.append(nums[i])
            if i == len(nums)-1:
                expectedNums.extend(["_"] * count)
        nums[:] = expectedNums
        k=len(nums)-count
        return k