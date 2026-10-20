class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        
        # Precompute divisors of n
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)
                    
        total_sum = 0
        
        for k in divisors:
            possible = True
            for i in range(0, n, k):
                block = nums[i:i+k]
                target = sorted_nums[i:i+k]
                
                # Fast cyclic rotation check:
                # Convert numbers to strings joined by a separator to avoid digit collision (e.g. '12' vs '1,2')
                block_str = ','.join(map(str, block)) + ','
                target_str = ','.join(map(str, target)) + ','
                
                # Doubling block_str allows us to find all rotations instantly via C-optimized substring search
                doubled_str = block_str + block_str[:-1]
                
                if target_str not in doubled_str:
                    possible = False
                    break
            
            if possible:
                total_sum += k
                
        return total_sum