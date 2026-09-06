# leetcode 121 : best time to buy and sell stock

#prices=[ 7,2,1,5,6,4,8 ]

#prices=[7,6,4,3,1]
#prices=[7,1,5,3,6,4]

prices = [2, 4, 1]

# 1. Start by assuming the first price is your lowest seen so far
min_price = prices[0]
max_profit = 0

# 2. Loop through every price in the array exactly once
for price in prices:
    # If we find a price lower than our minimum, update our minimum
    if price < min_price:
        min_price = price
    # Otherwise, check if selling today gives us a bigger profit than before
    elif price - min_price > max_profit:
        max_profit = price - min_price

print(max_profit)