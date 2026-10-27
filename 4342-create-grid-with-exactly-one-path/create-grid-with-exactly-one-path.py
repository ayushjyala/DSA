class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []
        
        # Row 0: All free cells
        grid.append('.' * n)
        
        # Rows 1 to m - 1: Obstacles everywhere except the last column
        for _ in range(1, m):
            grid.append('#' * (n - 1) + '.')
            
        return grid