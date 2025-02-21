class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas = sum(gas)
        totalCost = sum(cost)
        currentGas = 0
        answer = 0

        if totalGas < totalCost:
            return -1 

        for i in range(len(gas)):
            currentGas += gas[i] - cost[i]
            if currentGas < 0:
                answer = i+1 
                currentGas = 0 

        return answer