class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []
        open_brackets = {'(': ')', '[': ']', '{': '}'}
        
        for bracket in s:
            if bracket in open_brackets:
                stack.append(bracket)
            elif stack and bracket == open_brackets[stack[-1]]:
                stack.pop()
            else:
                return False
        
        return not stack