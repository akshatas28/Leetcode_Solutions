# leetcode 29 - divide 2 integers

#dividend=10
#divisor=3
dividend=7
divisor=-3

is_negative = (dividend < 0) ^ (divisor < 0)
dividend, divisor = abs(dividend), abs(divisor)
quotient = 0
INT_MIN = -2147483648
INT_MAX = 2147483647

while dividend >= divisor:
    shifts = 0
    while (divisor << (shifts + 1)) <= dividend:
        shifts += 1
    quotient += (1 << shifts)
    dividend -= (divisor << shifts)
if is_negative:
    quotient = -quotient

if quotient > INT_MAX:
    quotient = INT_MAX
elif quotient < INT_MIN:
    quotient = INT_MIN
print(quotient)