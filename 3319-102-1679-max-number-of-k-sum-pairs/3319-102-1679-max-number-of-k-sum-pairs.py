class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        answer = set()
        left = 0 
        right = len(nums)-1
        nums = sorted(nums)
        
        while left < right:
            comp = nums[left] + nums[right]
            if comp == k:
                answer.add((left, right))
                right-=1
                left+=1
            elif comp < k:
                left+=1
            elif comp >= k:
                right-=1
        
        return len(answer)