class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        maxKey = -100001
        minValue = 100001

        for num in nums:
            tempKey, tempValue = num, -(num) if num < 0 else num 
            if tempValue == minValue:
                maxKey = tempKey if tempKey > maxKey else maxKey
            elif tempValue < minValue:
                minValue = tempValue
                maxKey = tempKey

        return maxKey