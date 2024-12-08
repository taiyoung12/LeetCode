class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flat = sorted([item for row in matrix for item in row])
        return flat[k-1]
