import math
from typing import List


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            prod = 1
            g = 0
            lc = 1

            for j in range(i, n):
                x = nums[j]
                prod *= x
                g = x if g == 0 else math.gcd(g, x)
                lc = math.lcm(lc, x)

                if prod == lc * g:
                    ans = max(ans, j - i + 1)

        return ans