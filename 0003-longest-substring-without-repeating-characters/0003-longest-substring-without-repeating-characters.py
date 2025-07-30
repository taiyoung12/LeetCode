class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        answer = 1
        start = 0
        end = 1 

        while end < len(s):
            target = s[start:end+1]
            tempSet = len(set(target))
            tempLength = len(target)
            if tempSet == tempLength and tempLength > answer:
                answer = tempLength 
                end+=1
            else:
                start+=1
                end+=1

        return answer