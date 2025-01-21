def find_missing_number(arr, n):
    total = n * (n + 1) // 2
    return total - sum(arr)

# Example usage:
arr = [1, 2, 4, 6, 3, 7, 8]
n = 8
print(find_missing_number(arr, n))  # Output: 5
