class Solution:
    def possibleStringCount(self, word: str) -> int:
        answer = 1
        for i in range(1, len(word)):
            if word[i] == word[i-1]:
                answer+=1
        return answer 