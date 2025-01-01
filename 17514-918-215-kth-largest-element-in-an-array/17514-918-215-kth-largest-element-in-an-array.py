import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        targets = []

        for num in nums:
            heapq.heappush(targets, -num)
        
        for i in range(len(nums)):
            answer = heapq.heappop(targets)
            if i == k-1:
                return -answer