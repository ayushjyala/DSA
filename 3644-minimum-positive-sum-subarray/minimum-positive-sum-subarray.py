class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float('inf')
        
        # Check all possible subarray lengths from l to r
        for length in range(l, r + 1):
            # Check all subarrays of the current length
            for i in range(n - length + 1):
                current_sum = sum(nums[i:i + length])
                
                # We only care about sums strictly greater than 0
                if current_sum > 0:
                    min_sum = min(min_sum, current_sum)
                    
        return min_sum if min_sum != float('inf') else -1