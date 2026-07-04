class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # jumps = 0
        # current_end = 0
        # farthest = 0
        # for i in range(len(nums) - 1):
        #     farthest = max(farthest, i + nums[i])
        #     if i == current_end:
        #         jumps += 1
        #         current_end = farthest
        # return jumps
        n=len(nums)
        jump=0
        l=0
        r=0
        while r<n-1:
            farthest=0
            for i in range(l,r+1):
                farthest=max(i+nums[i],farthest)
            jump+=1
            l=r+1
            r=farthest
        return jump