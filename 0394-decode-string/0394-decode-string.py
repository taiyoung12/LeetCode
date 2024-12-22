class Solution:
    def decodeString(self, s: str) -> str:
        numbers = []
        strings = []
        current_number = 0
        current_string = ""

        for string in s: 
            if string.isdigit():
                current_number = current_number*10 + int(string)
            elif string == '[':
                numbers.append(current_number)
                strings.append(current_string)
                current_number = 0
                current_string = ""

            elif string == ']':
                number = numbers.pop()
                prev_string = strings.pop()

                current_string = prev_string + current_string * number
            else:
                current_string+=string
        
        return current_string