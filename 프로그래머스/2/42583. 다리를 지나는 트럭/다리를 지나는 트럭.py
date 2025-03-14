def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = [0]*bridge_length
    time = 0
    while q : 
        time+=1
        q.pop(0)
        if truck_weights : 
            if sum(q) + truck_weights[0] <= weight : 
                q.append(truck_weights.pop(0))
            else : 
                q.append(0)
    return time