# leetcode 58 - length of last word

#s = "Hello World"
#s="  fly me  to the moon  "
#s="  luffy is still joyboy"
#s="a"
#s="   day"
s="day"

s=s.rstrip()
count=0
i=len(s)-1

if len(s)==1:
    print(1)
else:
    while s[i]!=" " and i!=(-1):
        count+=1
        i-=1
    print(count)


# tc = O of N