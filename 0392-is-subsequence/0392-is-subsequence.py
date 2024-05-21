class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0 
        
        for i in range(len(t)) : 
            if len(s) == 0 :
                return True
            if s[s_index] == t[i] :
                s_index+=1
            if s_index == len(s):
                break
            
        return True if s_index == len(s) else False