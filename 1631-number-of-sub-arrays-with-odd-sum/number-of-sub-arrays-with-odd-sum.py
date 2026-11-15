class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        
        odd_count = 0
        even_count = 1  # Accounts for the initial prefix sum of 0 (which is even)
        prefix_sum = 0
        result = 0
        
        for num in arr:
            prefix_sum += num
            
            if prefix_sum % 2 == 1:
                # Current sum is odd; pair with all previous even prefix sums
                result += even_count
                odd_count += 1
            else:
                # Current sum is even; pair with all previous odd prefix sums
                result += odd_count
                even_count += 1
                
        return result % MOD