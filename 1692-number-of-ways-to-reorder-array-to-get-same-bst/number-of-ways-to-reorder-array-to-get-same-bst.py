class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod, n = 10**9 + 7, len(nums)
        
        # born[x] stores the index (insertion time) when value x appears in nums.
        # Walls 0 and n + 1 act as boundaries that appear "before time" (-1).
        born = [-1] * (n + 2)
        for t, x in enumerate(nums):
            born[x] = t
            
        sizes, stack = 1, [0]
        
        # Using a monotonic stack to find the left and right boundary (walls) for each element's subtree range.
        for v in range(1, n + 2):
            while born[stack[-1]] > born[v]:
                top = stack.pop()
                # The size of the valid subtree range for element `top` is determined by 
                # the current element `v` (right wall) and the element below `top` in stack (left wall).
                sizes = sizes * (v - stack[-1] - 1) % mod
            stack.append(v)
            
        # Precompute factorial modulo 10^9 + 7
        fact = 1
        for k in range(2, n + 1):
            fact = fact * k % mod
            
        # Total valid orderings = (n! * product of inverse subtree sizes) - 1 (excluding original array)
        return (fact * pow(sizes, -1, mod) - 1) % mod