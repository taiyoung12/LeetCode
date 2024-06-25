class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        x=0
        y=0
        answer = []
        answer.append(matrix[y][x])
        matrix[y][x] = 101
        

        for _ in range(0, len(matrix)*len(matrix[0])) :
            while x+1 < len(matrix[0]) and matrix[y][x+1] != 101 :
                x+=1 
                answer.append(matrix[y][x])
                matrix[y][x] = 101
            while y+1 < len(matrix) and matrix[y+1][x] !=101 : 
                y+=1
                answer.append(matrix[y][x])
                matrix[y][x]= 101

            while x-1 > -1 and matrix[y][x-1] != 101 :
                x-=1
                answer.append(matrix[y][x])
                matrix[y][x]=101

            while y-1 > -1 and matrix[y-1][x] !=101 : 
                y-=1
                answer.append(matrix[y][x])
                matrix[y][x]= 101                
        
        return answer