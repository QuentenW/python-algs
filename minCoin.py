#Find the minimum number of coins needed to make a given amount using denominations.

def min_coins(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        count += amount // coin
        amount %= coin
    return count if amount == 0 else -1

# Example
coins = [1, 2, 5, 10]
amount = 23
print("Minimum coins required:", min_coins(coins, amount))  # Output: 5
