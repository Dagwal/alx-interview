def makeChange(coins, total):
    if total <= 0:
        return 0
    
    # Initialize a list to store the minimum number of coins for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    for amount in range(1, total + 1):
        for coin in coins:
            if amount - coin >= 0:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    if dp[total] == float('inf'):
        return -1
    
    return dp[total]

# Test cases
print(makeChange([1, 2, 25], 37))
print(makeChange([1256, 54, 48, 16, 102], 1453))
