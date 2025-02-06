class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        target = dict()
        start = 0
        end = len(nums)
        answer = 0

        while start < end:
            comp = nums[start]
            for i in range(start+1, end):
                temp = comp * nums[i]
                if temp not in target:
                    target[temp] = [[comp, nums[i]]]
                else:
                    target[temp].append([comp, nums[i]])
            start+=1

        for t in target:
            if len(target[t]) > 1:
                e = (len(target[t])*(len(target[t])-1))//2
                answer+=(8*e)
        
        return answer