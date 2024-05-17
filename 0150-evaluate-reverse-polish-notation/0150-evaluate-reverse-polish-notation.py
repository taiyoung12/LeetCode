class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []        
        for token in tokens : 
            if token in operators : 
                right = stack.pop(-1)
                left = stack.pop(-1)
                if token == '+':
                    stack.append(left+right)
                if token == '-':
                    stack.append(left-right)
                if token == '*':
                    stack.append(left*right)
                if token == '/':                    
                    stack.append(int(left / right))
            else : 
                stack.append(int(token))
        
        return stack[0]