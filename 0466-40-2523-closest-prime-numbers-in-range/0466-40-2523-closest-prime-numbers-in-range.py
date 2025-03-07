import math 

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isPrime(number):
            if number < 2:
                return False
            if number == 2:
                return True
            if number % 2 == 0:
                return False
            
            for i in range(3, int(math.sqrt(number)) + 1, 2):
                if number % i == 0:
                    return False
            return True

        targets = []
        targetDict = {}

        for number in range(left, right+1):
            if isPrime(number):
                targets.append(number)
        
        for i in range(len(targets)-1):
            mi = targets[i+1] - targets[i]
            if mi in targetDict:
                continue
            elif mi not in targetDict:
                targetDict[mi] = [targets[i], targets[i+1]]

        if len(targetDict) < 1:
            return [-1, -1]

        minKey = min(targetDict)
        
        return targetDict[minKey]