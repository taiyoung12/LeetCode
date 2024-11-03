def solution(numbers, target):
    answer = 0
    comp = [0]
    
    for i in range(len(numbers)):
        temp = []
        for c in comp:
            temp.append(c + numbers[i])
            temp.append(c - numbers[i])
        comp = temp 
    
    for c in comp :
        if c == target:
            answer+=1
    
    return answer