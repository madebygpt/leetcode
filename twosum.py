class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # A dictionary to store the complement of each number
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if the complement exists in the dictionary
            if complement in num_map:
                # Return the indices of the two numbers
                return [num_map[complement], i]
            
            # Add the number and its index to the dictionary
            num_map[num] = i
        
        # No solution found, return an empty list
        return []
