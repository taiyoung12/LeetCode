class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        for number in range(1, n):
            target = s[:number]
            if target * (n // number) == s:
                return True 

        return False 