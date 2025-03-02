class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        target = {}

        for num in nums1:
            if num[0] not in target:
                target[num[0]] = [num[1]]
            else:
                target[num[0]].append(num[1])
        
        for num in nums2:
            if num[0] not in target:
                target[num[0]] = [num[1]]
            else:
                target[num[0]].append(num[1])
        
        target = dict(sorted(target.items(), key = lambda x:x[0]))

        answer = []

        for t in target:
            answer.append([t, sum(target[t])])

        return answer