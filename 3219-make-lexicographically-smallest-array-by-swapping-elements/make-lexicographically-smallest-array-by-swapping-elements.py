class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        arr = sorted((x, i) for i, x in enumerate(nums))
        ans = nums[:]

        start = 0

        for end in range(1, len(nums) + 1):
            if end == len(nums) or arr[end][0] - arr[end - 1][0] > limit:
                values = sorted(x for x, i in arr[start:end])
                indices = sorted(i for x, i in arr[start:end])

                for i in range(len(values)):
                    ans[indices[i]] = values[i]

                start = end

        return ans