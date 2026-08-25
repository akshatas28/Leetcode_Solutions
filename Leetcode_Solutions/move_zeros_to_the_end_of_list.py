# leetcode : problem 283 : Move zeros to the end of this list

count=0
i=0
n=len(nums)
while i <n:
    if nums[i]==0:
        count+=1
        nums.pop(i)
        n-=1
    else:
        i+=1

nums.extend([0]*count)