class Solution:
    def countCommas(self, n: int) -> int:
        # if n<1000:
        #     return 0
        # if n==1000:
        #     return 1
        # s=str(n)
        # length=len(s)
        # commas=length//3
        # digit=n-999
        # return digit*commas
        ans=0
        i=1000
        while i<=n:
            ans+=n-i+1
            i*=1000
        return ans