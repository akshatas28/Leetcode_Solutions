class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i= len(nums)-2
        temp=nums[len(nums)-1]
        def reversearray(nums, value, i, temp):
            if i == -1:
                nums[0]=temp
                return reversearray(nums, value+1, len(nums)-2, nums[len(nums)-1])
            if value==k+1:
                return nums
            nums[i+1] = nums[i]
            return reversearray(nums, value, i-1, temp)