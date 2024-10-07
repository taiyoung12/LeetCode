class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False 

        comp = dict()
        answer = ""

        for i in range(len(s)):
            comp[s[i]] = t[i]
        
        for v in s : 
            answer+=comp[v]

        return True if answer == t else False 