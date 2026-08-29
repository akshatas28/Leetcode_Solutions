# leetcode : problem 7 : reverse integers

#x=123 # 321
#x=-123 # -321
x=120 # 21

class Solution:
    def reverse(self, x: int) -> int:
        st=str(x)

        if x<0:
            p=(int(st[::-1].strip('-')))
            if p<=((2**31)-1) and p>=(-(2**31)):
                return (-p)
            else:
                return 0
        else:
            p=(int(st[::-1]))
            if p<=((2**31)-1) and p>=(-(2**31)):
                return (p)
            else:
                return 0