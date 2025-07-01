class Solution:
    def findLHS(self, nums: List[int]) -> int:
        targets = dict()
        answer = 0

        for num in nums:
            if num not in targets:
                targets[num]=1
            else:
                targets[num]+=1

        for target in targets:
            if target+1 in targets:
                answer = max(answer, targets[target] + targets[target+1])
            
        return answer