import itertools

def verify(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True 

def solution(nums):
    all = []
    answer = []
    
    for i in range(1, len(nums) + 1):
        permutations = itertools.permutations(nums, i)
        all.extend([''.join(p) for p in permutations])
    
    for a in all:
        if int(a) > 1 and verify(int(a)):
            while a[0] == "0":
                a = a[1:]
            if a in answer:
                continue
            answer.append(a)
    return len(answer)