class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        target = {}

        for gr in grid: 
            for i in range(len(gr)):
                if gr[i] not in target:
                    target[gr[i]] = 1
                else:
                    target[gr[i]] += 1
        
        sortTarget = dict(sorted(target.items()))
        
        comp = 1 
        answer = [0, 0]

        for ele in sortTarget:
            if sortTarget[ele] == 2:
                answer[0] = ele
            if ele != comp:
                answer[1] = (ele-1)
                comp+=1
            comp+=1
        
        if answer[1] == 0:
            answer[1] = len(target)+1

        return answer