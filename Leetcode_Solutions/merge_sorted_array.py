# leetcode : problem 88 : merge sorted array

nums1=[1,2,3,0,0,0]
nums2=[2,5,6]
m=3
n=3

nums1[:] = nums1[:m]

nums1.extend(nums2)
nums1.sort()
print(nums1)