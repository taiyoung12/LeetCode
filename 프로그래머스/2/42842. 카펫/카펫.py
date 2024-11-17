def solution(brown, yellow):
    target = brown + yellow 
    
    for t in range(1, target):
        comp = target // t
        if target % t !=0:
            continue 
        if comp <= t and (t-2)*(comp-2)==yellow:
            return [t, comp]