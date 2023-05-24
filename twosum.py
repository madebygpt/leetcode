def twoSum(nums, target):
    num_dict = {}  # Dictionary to store the complement of each number
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    
    return []  # No valid solution found

# Test the function with given examples
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # Output: [0, 1]

nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))  # Output: [1, 2]

nums = [3, 3]
target = 6
print(twoSum(nums, target))  # Output: [0, 1]
