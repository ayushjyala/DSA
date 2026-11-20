from collections import defaultdict
from typing import List

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        # dp[v] stores the longest consecutive sequence ending with value v
        dp = defaultdict(int)
        
        for x in nums:
            # Update x + 1 first so it uses the dp[x] from *earlier* elements
            dp[x + 1] = dp[x] + 1
            dp[x] = dp[x - 1] + 1
            
        return max(dp.values())