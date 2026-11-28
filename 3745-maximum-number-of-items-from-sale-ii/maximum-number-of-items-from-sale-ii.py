class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        freq = [0] * (n + 1)
        min_price = float('inf')
        
        for factor, price in items:
            freq[factor] += 1
            if price < min_price:
                min_price = price
                
        multiples_count = [0] * (n + 1)
        for f in range(1, n + 1):
            if freq[f] > 0:
                for m in range(f, n + 1, f):
                    multiples_count[f] += freq[m]
                    
        sorted_items = sorted(items, key=lambda x: x[1])
        
        ans = 0
        for factor, price in sorted_items:
            if price >= 2 * min_price:
                break
            gain = multiples_count[factor] - 1
            if gain > 0:
                take = min(gain, budget // price)
                ans += take * 2
                budget -= take * price
                
        ans += budget // min_price
        return ans