class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        # Adjust 0-based index i to 1-based index (i + 1)
        return sum(x ** 2 for i, x in enumerate(nums) if n % (i + 1) == 0)