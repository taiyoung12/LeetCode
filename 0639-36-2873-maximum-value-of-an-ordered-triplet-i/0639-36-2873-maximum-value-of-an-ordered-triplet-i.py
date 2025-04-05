class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        answer = 0
        length = len(nums)

        for i in range(length):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    comp = (nums[i]-nums[j])*nums[k]
                    answer = max(answer, comp)
        
        return answer 
        