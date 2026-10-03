class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(open_count: int, close_count: int, current_str: str):
            # Base case: valid string length reached
            if len(current_str) == 2 * n:
                res.append(current_str)
                return
            
            # Rule 1: We can add an open parenthesis if we haven't used 'n' of them yet
            if open_count < n:
                backtrack(open_count + 1, close_count, current_str + "(")
                
            # Rule 2: We can add a close parenthesis if there are unmatched open parentheses
            if close_count < open_count:
                backtrack(open_count, close_count + 1, current_str + ")")

        backtrack(0, 0, "")
        return res