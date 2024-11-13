def solution(routes):
    answer=1
    routes.sort(key = lambda x:x[1])
    cam = routes[0][1]
    for r in routes:
        if r[0] > cam:
            answer+=1
            cam=r[1]
    return answer