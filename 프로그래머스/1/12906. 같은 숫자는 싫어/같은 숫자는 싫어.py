def solution(arr):
    answer = [arr.pop(0)]
    
    for num in arr:
        if num != answer[-1]:
            answer.append(num)
    
    return answer