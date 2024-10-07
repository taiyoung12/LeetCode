class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words) or len(set(pattern)) != len(set(words)):
            return False 

        comp = dict()
        answer = ""

        for i in range(len(words)):
            comp[pattern[i]] = words[i]

        for p in pattern: 
            answer+= (comp[p] + " ")

        return True if answer == s + " " else False 