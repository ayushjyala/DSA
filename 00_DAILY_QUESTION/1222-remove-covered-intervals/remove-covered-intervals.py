class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        n=len(intervals)
        ans=0
        for i in range(n):
            covered=False
            for j in range(n):
                if i==j:
                    continue
                if intervals[j][0]<=intervals[i][0] and intervals[i][1]<=intervals[j][1]:
                    covered=True
                    continue
            if not covered:
                ans+=1
        return ans