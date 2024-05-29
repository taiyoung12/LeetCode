class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        isEnd = False 
        while isEnd is False : 
            if val in nums :
                nums.remove(val)
            else : 
                isEnd = True