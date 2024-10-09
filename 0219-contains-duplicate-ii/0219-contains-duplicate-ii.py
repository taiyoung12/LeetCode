class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        comp = dict()

        for i in range(len(nums)):
            if nums[i] in comp:
                if abs(comp[nums[i]] - i) <= k:
                    return True
            comp[nums[i]] = i

        return False