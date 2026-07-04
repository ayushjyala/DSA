class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_index=0
        for i in range(len(nums)):
            if (i>max_index):
                return False
            max_index=max(max_index,i+nums[i])
        return True