from queue import PriorityQueue

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = PriorityQueue()
        answer = []

        for point in points: 
            target = (point[0]*point[0] + point[1]*point[1])
            distance.put((target, point))
        
        for _ in range(0, k):
            answer.append(distance.get()[1])
            
        return answer 