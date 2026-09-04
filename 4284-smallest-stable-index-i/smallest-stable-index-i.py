class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # suffix minimum
        suffixMin = [0] * n
        suffixMin[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            suffixMin[i] = min(nums[i], suffixMin[i + 1])

        # prefix maximum
        prefixMax = nums[0]

        for i in range(n):
            prefixMax = max(prefixMax, nums[i])

            instability = prefixMax - suffixMin[i]

            if instability <= k:
                return i

        return -1