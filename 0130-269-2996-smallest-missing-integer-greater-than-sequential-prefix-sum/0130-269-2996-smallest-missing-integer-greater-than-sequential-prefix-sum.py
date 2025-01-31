class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        compIndex = 0
        targetSum = nums[0]
        for i in range(1, len(nums)):
            if(nums[i-1]+1 != nums[i]):
                compIndex = i
                break
            else:
                targetSum+=nums[i]

        while targetSum in nums:
            targetSum+=1
        
        return targetSum