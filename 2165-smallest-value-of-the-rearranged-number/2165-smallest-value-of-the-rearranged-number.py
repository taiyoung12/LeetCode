class Solution:
    def smallestNumber(self, num: int) -> int:
        nums = list(str(num))
        if len(nums) == 1 :
            return int(nums[0])
        
        answer = ""

        negative = True if num < 0 else False

        for i in range(len(nums)):
            if nums[i] != "-":
                nums[i] = int(nums[i])

        nums = sorted(nums[1:]) if negative else sorted(nums, reverse=True)
        
        if not negative: 
            index = -1
            while nums[index] == 0:
                index-=1

            if index != -1:
                nums[-1] = nums[index]
                nums[index] = 0
        
        for i in range(len(nums)-1, -1, -1) : 
            answer += str(nums[i])
    
        return -int(answer) if negative else int(answer)