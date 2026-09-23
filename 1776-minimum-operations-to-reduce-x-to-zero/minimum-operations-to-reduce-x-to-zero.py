class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        
        # If the total sum equals x, we must remove all elements
        if target == 0:
            return len(nums)
        # If target is negative, it's impossible to sum to x
        if target < 0:
            return -1
        
        max_len = -1
        current_sum = 0
        left = 0
        
        # Sliding window to find the longest subarray with sum equal to target
        for right in range(len(nums)):
            current_sum += nums[right]
            
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
                
            if current_sum == target:
                max_len = max(max_len, right - left + 1)
                
        return len(nums) - max_len if max_len != -1 else -1