#Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#01/2025, Quenten welch
def longest_consecutive_sequence(nums):
    if not nums:
        return 0

    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # Check if it's the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Count the length of the sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

# Test case
nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_sequence(nums))  # Output: 4
