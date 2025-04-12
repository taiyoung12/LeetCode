class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(set(nums)) == len(nums):
            return 0
    
        answer = 0

        for i in range(0, len(nums), 3):
            target = nums[i:]
            if len(set(target)) == len(target):
                return answer
            answer+=1 
        
        return answer 
