class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for star in s:
            if star != "*":
                stack.append(star)
            else:
                stack.pop(-1)
        
        return ''.join(stack)