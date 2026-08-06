class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            x = n
            prod = 1

            if x == 0:
                prod = 0
            else:
                while x:
                    prod *= x % 10
                    x //= 10

            if prod % t == 0:
                return n

            n += 1