# Given a sorted array of integers, find two numbers that add up to a specific target sum. Return their indices (1-based). Assume there's exactly one solution.

def find_pair_with_sum(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return left + 1, right + 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None  # If no pair is found (not needed here since one solution is guaranteed)

# Example
arr = [2, 7, 11, 15]
target = 9
print("Indices of pair with sum 9:", find_pair_with_sum(arr, target))  # Output: (1, 2)
