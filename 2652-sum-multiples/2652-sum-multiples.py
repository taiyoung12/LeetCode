class Solution:
    def sumOfMultiples(self, n: int) -> int:
        comp = [3, 5, 7]
        answer = 0

        for i in range(1, n+1):
            for div in comp: 
                if i % div == 0: 
                    answer += i
                    break
        
        return answer