def solution(nums):
    target = len(nums) // 2
    
    comp = dict()
    answer = 0
    
    for num in nums:
        if num not in comp:
            comp[num] = 1
            answer+=1
            if answer == target:
                return target
    
    return answer