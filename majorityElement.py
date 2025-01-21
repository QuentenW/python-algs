# Question: Write a function that finds the majority element in a list of integers. 
# The majority element is the element that appears more than n/2 times where n is the length of the list.
# Return the majority element, or None if no such element exists.

def majority_element(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
        if count[num] > len(nums) // 2:
            return num
    return None

# Example usage
print(majority_element([3, 3, 4, 2, 3, 3, 5]))  # Output: 3
