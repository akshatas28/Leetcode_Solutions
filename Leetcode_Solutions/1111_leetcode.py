class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        outputcount=0
        count=0
        nums=set(nums)
        for i in nums:
            if i-1 not in nums:
                current_num = i
                count = 1
                while current_num + 1 in nums:
                    count+=1
                    current_num+=1
            outputcount=max(outputcount,count)
        return (outputcount)