class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = sum(1 for num in nums if num > 0)
        neg = sum(1 for num in nums if num < 0)
        
        return max(pos, neg)