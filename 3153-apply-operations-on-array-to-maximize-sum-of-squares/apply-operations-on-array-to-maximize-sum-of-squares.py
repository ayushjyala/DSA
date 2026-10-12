class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        
        # Count set bits at each position (up to 30 bits for nums[i] <= 10^9)
        bit_count = [0] * 30
        for x in nums:
            for b in range(30):
                if (x >> b) & 1:
                    bit_count[b] += 1
        
        total_sum = 0
        
        # Form the k largest possible numbers
        for _ in range(k):
            val = 0
            for b in range(30):
                if bit_count[b] > 0:
                    val |= (1 << b)
                    bit_count[b] -= 1
            
            total_sum = (total_sum + val * val) % MOD
            
        return total_sum