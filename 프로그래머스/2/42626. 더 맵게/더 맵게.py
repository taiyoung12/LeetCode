import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        one = heapq.heappop(scoville)
        two = heapq.heappop(scoville)
        
        new_scoville = one + (two * 2)
        heapq.heappush(scoville, new_scoville)
        
        answer += 1
    
    return answer
