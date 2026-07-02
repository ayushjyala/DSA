class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        a=len(g)
        b=len(s)
        l=0
        r=0
        while (l<b and r<a):
            if g[r]<=s[l]:
                r+=1
            l+=1
        return r