#Find the maximum sum of a subarray with a fixed size k.

def max_sum_subarray(arr, k):
    max_sum = float('-inf')
    current_sum = 0
    for i in range(len(arr)):
        current_sum += arr[i]
        if i >= k - 1:
            max_sum = max(max_sum, current_sum)
            current_sum -= arr[i - (k - 1)]
    return max_sum

# Example
arr = [2, 3, 4, 1, 5]
k = 3
print("Max sum of subarray of size 3:", max_sum_subarray(arr, k))  # Output: 10
