class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # dp[j] will store the minimum cost to reach step j.
        # Since costs is 1-indexed and we need to go up to step n,
        # we can pad costs with a dummy element at index 0 to make it 1-indexed directly.
        c = [0] + costs
        
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for j in range(1, n + 1):
            # Try coming from j - 1, j - 2, j - 3
            for i in range(max(0, j - 3), j):
                jump_cost = c[j] + (j - i) ** 2
                dp[j] = min(dp[j], dp[i] + jump_cost)
                
        return dp[n]