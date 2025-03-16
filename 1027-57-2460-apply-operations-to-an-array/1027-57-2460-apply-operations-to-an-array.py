class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        length = len(nums)
        numbers = []

        for i in range(0, length-1):
            if nums[i] == nums[i+1]:
                target = nums[i]*2
                nums[i+1] = 0
                numbers.append(target)
            else:
                numbers.append(nums[i])
        
        numbers.append(nums[-1])
        newNumbers = []
        zeros = []

        for i in range(length):
            if numbers[i] == 0:
                zeros.append(0)
            else:
                newNumbers.append(numbers[i])
        
        return newNumbers + zeros