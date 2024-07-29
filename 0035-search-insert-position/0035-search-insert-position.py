class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        answer = -1
        for i, num in enumerate(nums):
            if num == target : 
                answer = i
                break 
            if num > target and answer == -1: 
                answer = i
                break
        
        return len(nums) if answer == -1 else answer 