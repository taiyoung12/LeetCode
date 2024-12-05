class Solution:
    def sortColors(self, nums: List[int]) -> None:
        start = 0 
        end = len(nums)

        for i in range(1, end):
            index = i
            while nums[index-1] > nums[index]:
                temp = nums[index]
                nums[index] = nums[index-1]
                nums[index-1] = temp
                if index > 1:
                    index-=1