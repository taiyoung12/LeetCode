class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x: x[1])
        answer = 0
        
        while points:
            point = points.pop(0)
            answer+=1
            while points and point[1] >= points[0][0]:
                points.pop(0)

        return answer