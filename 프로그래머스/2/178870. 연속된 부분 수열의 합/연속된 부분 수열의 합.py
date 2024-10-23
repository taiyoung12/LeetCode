def solution(sequence, k):
    answer = []
    start = 0 
    end = 0
    comp = sequence[start]
    n = len(sequence)
    min_index = 1000001
    
    while end < n:
        if comp < k:
            end+=1
            if end < n:
                comp +=sequence[end]
        elif comp == k:
            if min_index > end-start:
                min_index = end-start
                answer = [start, end]
            end+=1
            if end < n:
                comp +=sequence[end]
        elif comp > k:
            comp-=sequence[start]
            start+=1
    
    return answer