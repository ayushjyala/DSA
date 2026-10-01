class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        # Stack elements can be sets or operators like ',' and '{'
        stack = []
        
        for i, char in enumerate(expression):
            if char.isalpha():
                curr_set = {char}
                # Implicit concatenation: if previous element was a set, multiply them
                if stack and isinstance(stack[-1], set):
                    prev = stack.pop()
                    curr_set = {p + c for p in prev for c in curr_set}
                stack.append(curr_set)
                
            elif char == '{':
                # Check for implicit concatenation before opening brace
                if i > 0 and (expression[i - 1].isalpha() or expression[i - 1] == '}'):
                    stack.append('*')  # Explicit marker for concatenation
                stack.append('{')
                
            elif char == ',':
                stack.append(',')
                
            elif char == '}':
                # Process everything up to the matching '{'
                # Union all elements separated by ','
                expr_list = []
                while stack and stack[-1] != '{':
                    item = stack.pop()
                    if item != ',':
                        expr_list.append(item)
                
                stack.pop()  # Remove '{'
                
                # Combine all sets in expr_list with Union
                merged_set = set()
                for s in expr_list:
                    merged_set |= s
                
                # Handle implicit concatenation with whatever was before '{'
                if stack and stack[-1] == '*':
                    stack.pop()  # Remove '*' operator
                    prev = stack.pop()
                    merged_set = {p + m for p in prev for m in merged_set}
                elif stack and isinstance(stack[-1], set):
                    prev = stack.pop()
                    merged_set = {p + m for p in prev for m in merged_set}
                    
                stack.append(merged_set)

        # Final pass: Union all top-level sets remaining in stack
        res_set = set()
        while stack:
            item = stack.pop()
            if isinstance(item, set):
                res_set |= item

        return sorted(list(res_set))