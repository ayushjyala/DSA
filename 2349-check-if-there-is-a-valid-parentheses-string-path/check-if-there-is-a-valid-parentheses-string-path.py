from functools import lru_cache

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # 1. Total length of path must be even
        if (m + n - 1) % 2 != 0:
            return False
            
        # 2. Must start with '(' and end with ')'
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
            
        max_balance = (m + n) // 2

        @lru_cache(None)
        def dfs(r: int, c: int, balance: int) -> bool:
            # Update balance for current cell
            balance += 1 if grid[r][c] == '(' else -1
            
            # Invalid state: too many ')' or exceeds max possible '('
            if balance < 0 or balance > max_balance:
                return False
                
            # Reached bottom-right cell
            if r == m - 1 and c == n - 1:
                return balance == 0
            
            # Move right or down
            if c + 1 < n and dfs(r, c + 1, balance):
                return True
            if r + 1 < m and dfs(r + 1, c, balance):
                return True
                
            return False

        return dfs(0, 0, 0)