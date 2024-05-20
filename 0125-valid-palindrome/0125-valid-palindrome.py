class Solution:        
    def isPalindrome(self, s: str) -> bool:
        comps = ''
        result = True

        for c in s.lower() : 
            if c.isalpha() or c.isdigit():
                comps += c 

        if len(comps) % 2 == 0:
            left = len(comps) // 2 - 1
            right = len(comps) // 2
            while result and left > -1 and right < len(comps): 
                if comps[left] == comps[right]:
                    result = True
                    left -=1
                    right +=1
                else : 
                    result = False

        else : 
            left = len(comps) // 2
            right = len(comps) // 2
            while result and left > -1 and right < len(comps): 
                if comps[left] == comps[right]:
                    result = True
                    left -=1
                    right +=1
                else : 
                    result = False
        return result