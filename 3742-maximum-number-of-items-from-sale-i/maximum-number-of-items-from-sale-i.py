class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_f = max(f for f, _ in items)
        freq = [0] * (max_f + 1)
        for f, _ in items:
            freq[f] += 1

        divisible_count = [0] * (max_f + 1)
        for f in range(1, max_f + 1):
            if freq[f] > 0:
                for multiple in range(f, max_f + 1, f):
                    divisible_count[f] += freq[multiple]

        dp = [-10**9] * (budget + 1)
        dp[0] = 0
        min_price = 10**9

        for f, p in items:
            if p < min_price:
                min_price = p
            if p <= budget:
                first_copy_gain = divisible_count[f]
                for c in range(budget, p - 1, -1):
                    if dp[c - p] + first_copy_gain > dp[c]:
                        dp[c] = dp[c - p] + first_copy_gain

        ans = 0
        for c in range(budget + 1):
            if dp[c] >= 0:
                total = dp[c] + (budget - c) // min_price
                if total > ans:
                    ans = total

        return ans