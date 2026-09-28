# leetcode : 2149

newnums=[0]*len(nums)
positive=0
negative=1

for i in range(len(nums)):
    if nums[i]>0:
        newnums[positive]=nums[i]
        positive+=2
    elif nums[i]<0:
        newnums[negative]=nums[i]
        negative+=2
return (newnums)