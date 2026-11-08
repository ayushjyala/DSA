class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        row_count = [0] * m
        col_count = [0] * n
        
        # Step 1: Count servers in each row and column
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    row_count[r] += 1
                    col_count[c] += 1
                    
        communicating_servers = 0
        
        # Step 2: Count servers that share a row or column with another server
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (row_count[r] > 1 or col_count[c] > 1):
                    communicating_servers += 1
                    
        return communicating_servers