class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        temp = []
        for row in matrix : 
            if row[0] <= target and row[-1] >= target : 
                temp = row
                break 
        
        return target in temp
