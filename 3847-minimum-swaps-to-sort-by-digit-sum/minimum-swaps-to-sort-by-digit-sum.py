from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Helper function to compute digit sum
        def digit_sum(x):
            return sum(int(d) for d in str(x))
        
        # Create pairs of (digit_sum, value, original_index)
        indexed_nums = [(digit_sum(num), num, i) for i, num in enumerate(nums)]
        
        # Sort based on digit sum, then value
        sorted_indexed = sorted(indexed_nums)
        
        # Find the minimum swaps using cycle sort / visited tracking
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            # If already visited or already in the correct position
            if visited[i] or sorted_indexed[i][2] == i:
                continue
            
            # Traverse the cycle
            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                # Move to the index where the element that belongs here currently is
                curr = sorted_indexed[curr][2]
                cycle_size += 1
            
            if cycle_size > 1:
                swaps += (cycle_size - 1)
                
        return swaps