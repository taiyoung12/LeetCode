def solution(dirs):
    comp = [0, 0]
    visited_paths = set()
    answer = 0
    
    for dir in dirs:
        start = tuple(comp)
        
        if dir == "U" and comp[1] < 5:
            comp[1] += 1
        elif dir == "D" and comp[1] > -5:
            comp[1] -= 1
        elif dir == "R" and comp[0] < 5:
            comp[0] += 1
        elif dir == "L" and comp[0] > -5:
            comp[0] -= 1
        else:
            continue 
        
        end = tuple(comp)

        if (start, end) not in visited_paths and (end, start) not in visited_paths:
            visited_paths.add((start, end))
            answer += 1
    
    return answer
