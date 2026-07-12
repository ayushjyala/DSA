class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        d={}
        rank=1
        for num in sorted(set(arr)):
            d[num]=rank
            rank+=1
        ans=[]
        for num in arr:
            ans.append(d[num])
        return ans