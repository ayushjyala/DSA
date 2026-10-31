class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # Precompute destination when attempting to move RIGHT or DOWN from a mirror
        # mirror_right[r][c]: destination if entering mirror grid[r][c] while moving RIGHT
        # mirror_down[r][c]:  destination if entering mirror grid[r][c] while moving DOWN
        
        mirror_right = [[None] * n for _ in range(m)]
        mirror_down = [[None] * n for _ in range(m)]
        
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if grid[r][c] == 1:
                    # Moving RIGHT into mirror at (r, c) turns DOWN to (r + 1, c)
                    nr, nc = r + 1, c
                    if nr < m:
                        if grid[nr][nc] == 1:
                            mirror_right[r][c] = mirror_down[nr][nc]
                        else:
                            mirror_right[r][c] = (nr, nc)
                    else:
                        mirror_right[r][c] = None  # Out of bounds
                    
                    # Moving DOWN into mirror at (r, c) turns RIGHT to (r, c + 1)
                    nr, nc = r, c + 1
                    if nc < n:
                        if grid[nr][nc] == 1:
                            mirror_down[r][c] = mirror_right[nr][nc]
                        else:
                            mirror_down[r][c] = (nr, nc)
                    else:
                        mirror_down[r][c] = None  # Out of bounds

        def get_next(r: int, c: int, direction: int):
            """
            direction 0 = move RIGHT, 1 = move DOWN
            Returns (next_r, next_c) or None if out of bounds.
            """
            if direction == 0:
                nr, nc = r, c + 1
                if nc >= n:
                    return None
                if grid[nr][nc] == 1:
                    return mirror_right[nr][nc]
                return (nr, nc)
            else:
                nr, nc = r + 1, c
                if nr >= m:
                    return None
                if grid[nr][nc] == 1:
                    return mirror_down[nr][nc]
                return (nr, nc)

        # DP table: dp[r][c] stores number of valid paths to reach (r, c)
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for r in range(m):
            for c in range(n):
                if dp[r][c] == 0 or grid[r][c] == 1:
                    continue
                
                # Move Right
                target_right = get_next(r, c, 0)
                if target_right:
                    tr, tc = target_right
                    dp[tr][tc] = (dp[tr][tc] + dp[r][c]) % MOD
                
                # Move Down
                target_down = get_next(r, c, 1)
                if target_down:
                    tr, tc = target_down
                    dp[tr][tc] = (dp[tr][tc] + dp[r][c]) % MOD
                    
        return dp[m - 1][n - 1]