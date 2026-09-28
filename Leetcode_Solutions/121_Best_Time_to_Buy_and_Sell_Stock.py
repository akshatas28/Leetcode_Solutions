# leetcode : 121

low = float("inf")
profit=0
for i in range(0,len(prices)):
    low=min(low,prices[i])
    profit=max(profit, prices[i]-low)
 
return(profit)