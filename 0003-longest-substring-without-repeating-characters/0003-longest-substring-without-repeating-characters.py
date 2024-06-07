class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        comp = set(s)
        if len(comp) == len(s) : 
            return len(s)
        start = 0 
        end = 0 
        answer = 0
        
        while start < len(s) and end < len(s) : 
            comp = set(s[start:end+1])
            
            if len(comp) == len(s[start:end+1]) : 
                answer = max(answer, end-start+1)
                end+=1
            else : 
                start+=1

        return answer