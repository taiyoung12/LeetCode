class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran = dict()
        for key in magazine : 
            ran[key] = 1 if key not in ran else ran[key] + 1 
        
        for comp in ransomNote : 
            if comp in ran and ran[comp] > 0: 
                ran[comp]-=1
            else :
                return False 
        return True