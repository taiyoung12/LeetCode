class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(len(nums1)) : 
            if nums1[-1] == 0 :
                nums1.pop(-1)
            else :
                break
        
        nums1 += nums2
        nums1.sort(reverse=False)

        while len(nums1) < m+n : 
            nums1.append(0)