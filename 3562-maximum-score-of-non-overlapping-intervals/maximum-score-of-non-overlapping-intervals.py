class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n=len(intervals)

        arr=[]

        for i in range(n):
            l,r,w=intervals[i]
            arr.append((l,r,w,i))

        arr.sort()

        starts=[]

        for x in arr:
            starts.append(x[0])

        import bisect

        nxt=[0]*n

        for i in range(n):
            nxt[i]=bisect.bisect_right(starts,arr[i][1])

        dp={}

        def solve(i,k):
            if i==n or k==4:
                return (0,())

            if (i,k) in dp:
                return dp[(i,k)]

            score1,ans1=solve(i+1,k)

            j=nxt[i]

            score2,ans2=solve(j,k+1)
            score2+=arr[i][2]
            ans2=(arr[i][3],)+ans2

            if score2>score1:
                dp[(i,k)]=(score2,ans2)
            elif score2<score1:
                dp[(i,k)]=(score1,ans1)
            else:
                a=tuple(sorted(ans1))
                b=tuple(sorted(ans2))

                if b<a:
                    dp[(i,k)]=(score2,ans2)
                else:
                    dp[(i,k)]=(score1,ans1)

            return dp[(i,k)]

        score,ans=solve(0,0)

        return sorted(ans)