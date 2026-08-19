class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}
        for r, s in reservedSeats:
            if 2 <= s <= 9:
                rows[r] = rows.get(r, 0) | (1 << (s - 2))
        ans = (n - len(rows)) * 2
        left = 15     
        middle = 60   
        right = 240   
        for mask in rows.values():
            if (mask & left) == 0 and (mask & right) == 0:
                ans += 2
            elif (mask & left) == 0 or (mask & middle) == 0 or (mask & right) == 0:
                ans += 1
        return ans