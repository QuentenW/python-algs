# Question: Write a function to find the length of the longest contiguous subarray with a target sum.

def longest_subarray_with_sum(nums, target):
    prefix_sum = {}
    current_sum = 0
    max_length = 0
    
    for i, num in enumerate(nums):
        current_sum += num
        if current_sum == target:
            max_length = i + 1
        if current_sum - target in prefix_sum:
            max_length = max(max_length, i - prefix_sum[current_sum - target])
        if current_sum not in prefix_sum:
            prefix_sum[current_sum] = i
    
    return max_length

# Example usage
print(longest_subarray_with_sum([1, -1, 5, -2, 3], 3))  # Output: 4
