class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        row = []
        for i in range(len(matrix)) : 
            row_in = []
            for j in range(len(matrix[i])-1, -1, -1) :
                row_in.append(matrix[j][i])
            row.append(row_in)
        matrix[:] = row