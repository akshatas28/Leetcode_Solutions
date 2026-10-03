# leetcode : 128 - longest consecutive sequence 

nums=[1,99,101,98,2,5,3,100,1,1]
#nums=[100,4,200,1,3,2]
#nums=[0,3,7,2,5,8,4,6,0,1]
#nums=[1,0,1,2]
count=0
outputcount=0
nums=set(nums)

# this solution is considered O(n) time with a set, and O(n²) with a list.

for i in nums:
    if i-1 not in nums:
        current_num = i
        count = 1
        while current_num + 1 in nums:
            count+=1
            current_num+=1
    outputcount=max(outputcount,count)
print(outputcount)