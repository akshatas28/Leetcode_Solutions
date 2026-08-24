# leetcode : problem 125 : valid palindrome

s = "A man, a plan, a canal: Panama"

temp = "".join(char.lower() for char in s if char.isalnum())

temprev=temp[::-1]
print(temprev)

if temp==temprev:
    return True
else:
    return False