class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # Check if the sum is out of the valid range
        if sum < 1 or sum > 9 * num:
            return ""
        
        res = []
        for i in range(num):
            # Take as much as possible for the current leftmost position
            cur = min(9, sum)
            res.append(str(cur))
            sum -= cur
            
        return "".join(res)