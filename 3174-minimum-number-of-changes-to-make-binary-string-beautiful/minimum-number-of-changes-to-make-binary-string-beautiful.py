class Solution:
    def minChanges(self, s: str) -> int:
        changes = 0
        
        # Iterate through the string in steps of 2
        for i in range(0, len(s), 2):
            # If the adjacent pair doesn't match, 1 change is needed
            if s[i] != s[i + 1]:
                changes += 1
                
        return changes