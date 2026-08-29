# leetcode : problem 485 : MAX CONSECUTIVE ONES


maxcount=0
count=0
i=0
while i<len(nums):
    if nums[i]==1:
        count+=1
        i+=1
    else:
        count=0
        i+=1
    if count>maxcount:
        maxcount=count
    
print(maxcount)