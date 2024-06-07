class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target : 
            return 0 
        sub_sum = 0
        answer = 999999
        start = 0 

        for end in range(len(nums)) : 
            sub_sum += nums[end]

            while sub_sum >= target : 
                answer = min(answer, end-start+1)
                sub_sum -= nums[start]
                start+=1

        return answer  