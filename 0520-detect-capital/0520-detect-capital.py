class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper():
            return True 
        
        for i in range(len(word)-1, 0, -1):
            if word[i].isupper():
                return False 
        
        return True