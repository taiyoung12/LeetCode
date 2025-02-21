def solution(array, commands):
    answer = []
    
    for command in commands: 
        target = sorted(array[command[0]-1:command[1]])
        answer.append(target[command[2]-1])
        
    return answer