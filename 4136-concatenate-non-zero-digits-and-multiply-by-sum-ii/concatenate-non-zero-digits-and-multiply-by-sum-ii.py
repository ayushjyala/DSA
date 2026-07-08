class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # ans=[]
        # result=[]
        # summ=0
        # for num in queries:
        #     for i in range(num[0],num[1]+1):
        #         i=''.join(s)
        #         for ch in s:
        #             if ch!='0':
        #                 ans.append(ch)
        #         for ch in i:
        #             summ+=int(ch)
        #     result.append(summ*ans)
        # return result

        # mod=(10**9)+7
        # result=[]
        # for num in queries:
        #     ans=""
        #     summ=0
        #     i=s[num[0]:num[1]+1]
        #     for ch in i:
        #         if ch!=0:
        #             ans+=ch
        #     if ans=="":
        #         result.append(0)
        #         continue
        #     for ch in ans:
        #         summ+=int(ch)
        #     result.append((int(ans)*summ)%mod)
        # return result

        # mod=10**9+7
        # result=[]
        # for num in queries:
        #     ans=""
        #     summ=0
        #     i=s[num[0]:num[1]+1]
        #     for ch in i:
        #         if ch!='0':
        #             ans+=ch
        #     if ans=="":
        #         result.append(0)
        #         continue
        #     for ch in ans:
        #         summ+=int(ch)
        #     result.append((int(ans)*summ)%mod)
        # return result

        MOD=10**9+7
        pos=[]
        digit=[]
        for i,ch in enumerate(s):
            if ch!='0':
                pos.append(i)
                digit.append(ord(ch)-48)
        k=len(pos)
        if k==0:
            return [0]*len(queries)
        prefSum=[0]*(k+1)
        prefHash=[0]*(k+1)
        for i in range(1,k+1):
            prefSum[i]=prefSum[i-1]+digit[i-1]
            prefHash[i]=(prefHash[i-1]*10+digit[i-1])%MOD
        pow10=[1]*(k+1)
        for i in range(1,k+1):
            pow10[i]=(pow10[i-1]*10)%MOD
        def lower(x):
            l=0
            r=k
            while l<r:
                m=(l+r)//2
                if pos[m]<x:
                    l=m+1
                else:
                    r=m
            return l
        def upper(x):
            l=0
            r=k
            while l<r:
                m=(l+r)//2
                if pos[m]<=x:
                    l=m+1
                else:
                    r=m
            return l
        ans=[]
        for l,r in queries:
            L=lower(l)
            R=upper(r)-1
            if L>R:
                ans.append(0)
                continue
            cnt=R-L+1
            sm=prefSum[R+1]-prefSum[L]
            x=(prefHash[R+1]-prefHash[L]*pow10[cnt])%MOD
            ans.append((x*sm)%MOD)
        return ans