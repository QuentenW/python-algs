def min_path_sum(grid):
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    
    # Initialize the DP table with the same dimensions as the grid
    dp = [[0] * n for _ in range(m)]
    
    # Base case: starting point
    dp[0][0] = grid[0][0]
    
    # Fill the first row (can only come from the left)
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    
    # Fill the first column (can only come from above)
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(dp[i - 1][j], dp[i][j-1]) + grid[i][j]
    print("DP", dp)
    return dp

# Example grid
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

# Function call
print(min_path_sum(grid))  # Expected output is 7


