class Solution:
    def findKthSmallest(self, coins, k):
        coins.sort()

        # Remove redundant coins (e.g., 6 if 3 already exists)
        arr = []
        for c in coins:
            ok = True
            for d in arr:
                if c % d == 0:
                    ok = False
                    break
            if ok:
                arr.append(c)

        coins = arr
        n = len(coins)

        high = coins[0] * k
        limit = high + 1

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        lcm = [1] * (1 << n)

        for mask in range(1, 1 << n):
            bit = mask & -mask
            idx = bit.bit_length() - 1
            prev = mask ^ bit

            val = lcm[prev]
            if val > high:
                lcm[mask] = limit
            else:
                g = gcd(val, coins[idx])
                x = val // g * coins[idx]
                if x > high:
                    x = limit
                lcm[mask] = x

        def count(x):
            ans = 0
            for mask in range(1, 1 << n):
                v = lcm[mask]
                if v <= x:
                    if mask.bit_count() & 1:
                        ans += x // v
                    else:
                        ans -= x // v
            return ans

        lo, hi = 1, high
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo