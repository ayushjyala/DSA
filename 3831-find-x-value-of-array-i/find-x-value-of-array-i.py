class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result=[0]*k
        dp=[0]*k

        for nuii in nums:
            new_dp=[0]*k

            new_dp[nuii%k]+=1

            for r in range(k):
                new_r=(r*(nuii%k))%k
                new_dp[new_r]+=dp[r]

            for r in range(k):
                result[r]+=new_dp[r]

            dp=new_dp

        return result