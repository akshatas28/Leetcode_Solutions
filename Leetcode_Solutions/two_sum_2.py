# leetcode : problem 1 : TWO SUM

#nums=[ 5,9,1,2,4,15,6,3 ]
#nums=[ 2,7,11,15 ]
#nums=[ 3,2,4 ]
nums=[ 3,2,3 ]

target=6

d1={}
for i in range(0,len(nums)):
    remaining= target-nums[i]
    if remaining in d1:
        return(d1[remaining],i)
    d1[nums[i]] =i

#print(d1)
#print(maxcount)