class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # dp[j] stores a bitmask where the k-th bit is 1 if XOR value k is reachable at column j
        dp = [0] * n
        
        # Initialize first cell
        x = grid[0][0]
        dp[0] = 1 << x
        
        # Initialize first row
        for j in range(1, n):
            x ^= grid[0][j]
            dp[j] = 1 << x
            
        # Process row by row
        for i in range(1, m):
            # First column of current row depends only on the cell above
            prev_mask = dp[0]
            new_mask = 0
            val = grid[i][0]
            
            mask = prev_mask
            while mask:
                lsb = mask & -mask
                xor_val = (lsb).bit_length() - 1
                new_mask |= 1 << (xor_val ^ val)
                mask ^= lsb
            dp[0] = new_mask
            
            for j in range(1, n):
                # Reachable XORs come from top (dp[j]) and left (dp[j-1])
                prev_mask = dp[j] | dp[j - 1]
                
                new_mask = 0
                val = grid[i][j]
                
                mask = prev_mask
                while mask:
                    lsb = mask & -mask
                    xor_val = (lsb).bit_length() - 1
                    new_mask |= 1 << (xor_val ^ val)
                    mask ^= lsb
                    
                dp[j] = new_mask

        # Find the minimum possible XOR value from the final bitmask at bottom-right cell
        final_mask = dp[n - 1]
        
        # Find the lowest set bit in final_mask which corresponds to the minimum XOR value
        min_xor = 0
        while final_mask:
            lsb = final_mask & -final_mask
            min_xor = lsb.bit_length() - 1
            break
            
        return min_xor