# leetcode 35 - search insert position

nums=[1,3,5,6]
#target=5
#target=2
target=7
left=0
right=len(nums)-1

for i in range(len(nums)):
    if nums[i]==target:
        print(i)
        break
    elif target>nums[right]:
        print(len(nums))
        break
    elif target<nums[left]:
        print(0)
        break
    else:
        while left<right:
            if target>nums[left]:
                left+=1
                if nums[left]>target:
                    print(left)
            elif target<nums[right]:
                right-=1
                if nums[right]<target:
                    print(right)
        
# tc must be O(log n)

# leetcode 35 - search insert position

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left=0
        right=len(nums)-1
        
        for i in range(len(nums)):
            if nums[i]==target:
                return (i)
                break
            elif target>nums[right]:
                return (len(nums))
                break
            elif target<nums[left]:
                return (0)
                break
            else:
                while left<right:
                    if target>nums[left]:
                        left+=1
                        if nums[left]>target:
                            return (left)
                    elif target<nums[right]:
                        right-=1
                        if nums[right]<target:
                            return (right)