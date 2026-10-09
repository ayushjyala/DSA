class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open_needed = 0  # Number of ')' needed
        
        for char in s:
            if char == '(':
                # If open_needed is odd, we have an unmatched single ')' before '('
                if open_needed % 2 != 0:
                    insertions += 1  # Add one ')'
                    open_needed -= 1  # Completed the pair
                open_needed += 2
            else:  # char == ')'
                open_needed -= 1
                # If we encounter ')' without a matching '(', add a '('
                if open_needed < 0:
                    insertions += 1  # Insert '('
                    open_needed += 2  # The inserted '(' needs 2 ')'s, one is consumed by current ')'
                    
        return insertions + open_needed