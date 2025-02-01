def solution(arr1, arr2):
    answer = []
    row, col, col2 = len(arr1), len(arr1[0]), len(arr2[0])
    
    for i in range(row):
        arr1Row = arr1[i]
        target = []
        for j in range(col2):
            comp = 0
            for n in range(col):
                comp += arr1Row[n] * arr2[n][j]
            target.append(comp)
        answer.append(target)
    
    return answer