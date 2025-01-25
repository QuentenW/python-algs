#Generate all subsets of a given list.

def subsets(nums):
    result = []
    def backtrack(start, path):
        result.append(path)
        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]])
    backtrack(0, [])
    return result

# Example
nums = [1, 2, 3]
print("Subsets:", subsets(nums))
