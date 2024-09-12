class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        n = 0
        number = 0
        for digit in digits : 
            number += digit * (10**n)
            n+=1
        number+=1

        return list(map(int,str(number)))