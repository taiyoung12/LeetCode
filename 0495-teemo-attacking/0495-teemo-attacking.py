class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        length = len(timeSeries)
        if length == 0:
            return 0
        
        answer = 0
        for i in range(length-1):
            answer += min(timeSeries[i+1]-timeSeries[i], duration)
        return answer + duration