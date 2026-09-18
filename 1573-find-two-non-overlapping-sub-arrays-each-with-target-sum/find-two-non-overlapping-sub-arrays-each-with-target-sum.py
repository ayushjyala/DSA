class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        min_len = [float('inf')] * n
        
        ans = float('inf')
        current_sum = 0
        left = 0
        best_till_now = float('inf')
        
        for right in range(n):
            current_sum += arr[right]
            
            # Shrink window if sum exceeds target
            while current_sum > target:
                current_sum -= arr[left]
                left += 1
                
            # Valid subarray found
            if current_sum == target:
                current_len = right - left + 1
                
                # Check if there is a non-overlapping valid subarray to the left
                if left > 0 and min_len[left - 1] != float('inf'):
                    ans = min(ans, current_len + min_len[left - 1])
                
                best_till_now = min(best_till_now, current_len)
            
            min_len[right] = best_till_now
            
        return ans if ans != float('inf') else -1