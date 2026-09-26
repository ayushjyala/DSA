class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Step 1: Build the lookup dictionary
        lookup = {k: v for k, v in knowledge}
        
        res = []
        in_bracket = False
        key_buffer = []
        
        # Step 2: Single pass over string s
        for ch in s:
            if ch == '(':
                in_bracket = True
                key_buffer = []
            elif ch == ')':
                in_bracket = False
                key = "".join(key_buffer)
                res.append(lookup.get(key, "?"))
            elif in_bracket:
                key_buffer.append(ch)
            else:
                res.append(ch)
                
        return "".join(res)