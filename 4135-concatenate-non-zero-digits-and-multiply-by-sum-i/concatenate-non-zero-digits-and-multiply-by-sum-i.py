class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        # s=str(n)
        # ans=[]
        # summ=0
        # for num in s:
        #     summ+=int(num)
        # for num in s:
        #     if num!='0':
        #         ans.append(num)
            
        # x=''.join(ans)
        # return(summ*int(x))
        s = str(n)
        ans = []

        for ch in s:
            if ch != '0':
                ans.append(ch)

        if not ans:
            return 0

        x = ''.join(ans)
        summ = 0

        for ch in x:
            summ += int(ch)

        return int(x) * summ