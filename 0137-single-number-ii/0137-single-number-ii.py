class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_ = dict()

        for n in nums:
            if n not in hash_:
                hash_[n] = 1
            else:
                hash_[n] += 1

        for h in hash_:
            if hash_[h] == 1:
                return h

        return -1