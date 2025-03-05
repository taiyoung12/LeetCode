class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        answer = []
        while n > 0:
            target = 1 
            count = 1 
            while n > target:
                if target*3 > n:
                    break
                else:
                    target*=3
                    count+=1
            n-=target
            answer.append(count)
        
        return True if len(answer) == len(set(answer)) else False 