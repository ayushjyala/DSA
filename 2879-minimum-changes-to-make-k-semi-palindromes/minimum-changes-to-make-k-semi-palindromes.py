class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        # Precompute proper divisors for all possible substring lengths (2 to n)
        divisors = [[] for _ in range(n + 1)]
        for length in range(2, n + 1):
            for d in range(1, length // 2 + 1):
                if length % d == 0:
                    divisors[length].append(d)
        
        # Helper function to find min changes to make s[i..j] a semi-palindrome
        def get_cost(i: int, j: int) -> int:
            length = j - i + 1
            min_changes = float('inf')
            
            for d in divisors[length]:
                changes = 0
                # Check each of the d interleaved groups
                for offset in range(d):
                    left = i + offset
                    right = j - (d - 1 - offset)
                    while left < right:
                        if s[left] != s[right]:
                            changes += 1
                        left += d
                        right -= d
                if changes < min_changes:
                    min_changes = changes
                    
            return min_changes

        # Precompute cost[i][j] for all valid substrings (length >= 2)
        cost = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                cost[i][j] = get_cost(i, j)
        
        # dp[p][i] = min changes to partition prefix of length i into p semi-palindromes
        dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]
        
        # Base case: 1 partition
        for i in range(2, n + 1):
            dp[1][i] = cost[0][i - 1]
            
        # Fill DP table for 2 to k partitions
        for p in range(2, k + 1):
            for i in range(2 * p, n + 1):
                for m in range(2 * (p - 1), i - 1):
                    if dp[p - 1][m] + cost[m][i - 1] < dp[p][i]:
                        dp[p][i] = dp[p - 1][m] + cost[m][i - 1]
                        
        return dp[k][n]