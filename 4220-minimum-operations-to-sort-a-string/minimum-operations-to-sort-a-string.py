class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        
        # Check if already sorted
        if list(s) == sorted(s):
            return 0
        
        # Length 2 unsorted is impossible
        if n == 2:
            return -1
        
        min_char = min(s)
        max_char = max(s)
        
        # 1 operation
        if s[0] == min_char or s[-1] == max_char:
            return 1
        
        # 3 operations
        max_only_at_0 = (s[0] == max_char) and (max_char not in s[1:])
        min_only_at_n1 = (s[-1] == min_char) and (min_char not in s[:-1])
        
        if max_only_at_0 and min_only_at_n1:
            return 3
            
        return 2