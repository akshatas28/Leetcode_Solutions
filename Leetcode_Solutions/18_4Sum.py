# leetcode 18 - 4SUM


nums.sort()
n=len(nums)
result=[]

for j in range(n-3):
    if j>0 and nums[j]==nums[j-1]:
        continue
    for i in range(j+1,n-2):
        if i>j+1 and nums[i]==nums[i-1]:
            continue
        left=i+1
        right=n-1
        while left<right:
            currentsum=nums[j]+nums[i]+nums[left]+nums[right]
            if currentsum==target:
                result.append([nums[j],nums[i],nums[left],nums[right]])
                left+=1
                right-=1
                while left < right and nums[left] == nums[left - 1]:
                    left+=1
                while left < right and nums[right] == nums[right + 1]:
                    right-=1
            elif currentsum<target:
                left+=1
            else:
                right-=1

print(result)