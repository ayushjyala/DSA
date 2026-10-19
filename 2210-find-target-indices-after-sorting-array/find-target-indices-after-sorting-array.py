class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        smaller_count = 0
        target_count = 0
        
        for num in nums:
            if num < target:
                smaller_count += 1
            elif num == target:
                target_count += 1
                
        # Generate the list of indices starting from smaller_count
        return list(range(smaller_count, smaller_count + target_count))