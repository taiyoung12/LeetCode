class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        targets = {}
        maxCount = 0 
        maxLength = 0
        start = 0 

        for i in range(len(s)):
            if s[i] not in targets:
                targets[s[i]]=1
            else:
                targets[s[i]]+=1
            
            maxCount = max(maxCount, targets[s[i]])

            if (i - start + 1) - maxCount > k:
                targets[s[start]]-=1
                start+=1
            
            maxLength = max(maxLength, i - start + 1)
        
        return maxLength