class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        ans=[]
        s="123456789"
        for l in range(len(str(low)),len(str(high))+1):
            for i in range(10-l):
                num=int(s[i:i+l])
                if low<=num<=high:
                    ans.append(num)
        return ans