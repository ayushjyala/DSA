class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a

        pre=[]
        mx=0

        for x in nums:
            if x>mx:
                mx=x
            pre.append(gcd(x,mx))

        pre.sort()

        ans=0
        i=0
        j=len(pre)-1

        while i<j:
            ans+=gcd(pre[i],pre[j])
            i+=1
            j-=1

        return ans