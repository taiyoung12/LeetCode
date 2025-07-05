class Solution:
    def findLucky(self, arr: List[int]) -> int:
        targets = {}
        answer = 0

        for number in arr:
            if number not in targets:
                targets[number] = 1
            else : 
                targets[number] += 1
        
        for k, v in targets.items():
            if k == v:
                answer = max(answer, k)

        return -1 if answer == 0 else answer