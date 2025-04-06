class Solution:
    def isPalindrome(self, x: int) -> bool:
        xList = list(str(x))
        xReverse = xList[::-1]
        
        return True if xList == xReverse else False 