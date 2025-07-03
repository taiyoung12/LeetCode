class Solution:
    def kthCharacter(self, k: int) -> str:
        string = "a"

        while len(string) <= k:
            temp = string

            for char in string:
                if char == 'z':
                    temp += 'a'
                else:
                    temp += chr(ord(char) + 1)
            
            string = temp      

        return string[k - 1]