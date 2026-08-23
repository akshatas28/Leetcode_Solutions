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

# Do one more submission for leetcode 26


num=[1, 2, 2, 2, 3]
index=1
count=0
for i in range(1, len(num)):
    if num[i] != num[i-1] :
        num[index] = num[i]
        index+=1
    else:
        count+=1
#num[:] = [x for x in num if x != '_']
num[index:] = ["_"] * count
print(num)