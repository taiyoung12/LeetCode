class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = nums[0]
        last = nums[-1]
        
        for i in range(start, last+1):
            comp = nums.count(i)
            if comp > 2 :
                for _ in range(comp-2) : 
                    nums.remove(i)