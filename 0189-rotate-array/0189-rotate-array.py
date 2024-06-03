class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        e = k % len(nums)
        
        out = nums[0:len(nums)-e]
        del nums[0:len(nums)-e]
        nums+=out