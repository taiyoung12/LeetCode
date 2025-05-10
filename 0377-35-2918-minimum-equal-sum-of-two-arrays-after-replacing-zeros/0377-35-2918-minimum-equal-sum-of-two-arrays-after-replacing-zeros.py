class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        zero1, zero2 = nums1.count(0), nums2.count(0)

        min_possible1 = sum1 + zero1 * 1
        max_possible1 = sum1 + zero1 * 10**9
        min_possible2 = sum2 + zero2 * 1
        max_possible2 = sum2 + zero2 * 10**9

        min_common = max(min_possible1, min_possible2)
        max_common = min(max_possible1, max_possible2)

        if min_common > max_common:
            return -1
        else:
            return min_common