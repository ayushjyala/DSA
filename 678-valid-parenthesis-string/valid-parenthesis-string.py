class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0
        
        for ch in s:
            if ch == '(':
                low += 1
                high += 1
            elif ch == ')':
                low -= 1
                high -= 1
            else:  # ch == '*'
                low -= 1
                high += 1
            
            # More ')' than possible '(' + '*'
            if high < 0:
                return False
            
            # Count of open brackets cannot drop below 0
            if low < 0:
                low = 0
                
        return low == 0