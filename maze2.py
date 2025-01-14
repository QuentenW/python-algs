grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
 m, n = len(grid), len(grid[0])

 dpGrid = [[0] * n for _ in range(m)]

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