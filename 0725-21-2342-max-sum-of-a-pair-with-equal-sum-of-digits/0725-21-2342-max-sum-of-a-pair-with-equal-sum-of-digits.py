class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        comps = dict()
        answer = []

        for i in range(len(nums)):
            target = nums[i]
            targetSum = 0
            while target != 0:
                t = target%10
                targetSum+=t
                target = target//10
            if targetSum not in comps:
                comps[targetSum] = [nums[i]]
            else:
                comps[targetSum].append(nums[i])

        maxSum = -1

        for targetSum, values in comps.items():
            if len(values) > 1:
                values.sort(reverse=True)
                maxSum = max(maxSum, values[0]+values[1])

        return maxSum