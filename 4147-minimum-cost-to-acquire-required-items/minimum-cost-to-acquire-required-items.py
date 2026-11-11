class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # Minimum requirement shared by both
        common_need = min(need1, need2)
        
        # Remaining requirement for individual items
        rem1 = need1 - common_need
        rem2 = need2 - common_need
        
        # Cost to cover common requirement
        ans = common_need * min(costBoth, cost1 + cost2)
        
        # Cost to cover remaining individual requirements
        ans += rem1 * min(cost1, costBoth)
        ans += rem2 * min(cost2, costBoth)
        
        return ans