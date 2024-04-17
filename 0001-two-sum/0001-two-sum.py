class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        test = {}
        for i in range(len(nums)) :
            r = sorted([nums[i], target-nums[i]])
            e = str(r[0]) + str(r[1])
            if e in test : 
                test[e].append(i)
            else : 
                test[e] = []
                test[e].append(i)
        for j in test : 
            if len(test[j]) == 2 :
                output = test[j]
        return output