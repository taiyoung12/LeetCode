class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for string in s : 
            if string.isdigit():
                if stack:
                    stack.pop(-1)
            else:
                stack.append(string)
        
        return ''.join(stack)