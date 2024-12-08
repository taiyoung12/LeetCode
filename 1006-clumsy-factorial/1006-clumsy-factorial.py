class Solution:
    def clumsy(self, n: int) -> int:
        stack = [n]
        n-=1
        index = 0

        while n>0:
            if index%4 == 0:
                stack.append(stack.pop() * n)
            if index%4 == 1:
                prev = stack.pop()
                if prev < 0:
                    stack.append(-(-prev // n))
                else:
                    stack.append(prev // n)
            if index%4 == 2:
                stack.append(n)
            if index%4 == 3:
                stack.append(-n)
            n-=1
            index+=1
        
        return sum(stack)