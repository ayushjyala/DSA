class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total = 0
        has_non_zero = False

        for x in nums:
            total ^= x
            if x != 0:
                has_non_zero = True

        if total != 0:
            return len(nums)
        if has_non_zero:
            return len(nums) - 1
        return 0