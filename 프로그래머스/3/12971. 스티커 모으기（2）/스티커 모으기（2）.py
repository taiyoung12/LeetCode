def solution(stickers):
    if len(stickers)==1:
        return stickers[0]

    dp1 = [0] + stickers[:-1]
    dp2 = [0] + stickers[1:]
    
    for i in range(2, len(stickers)):
        dp1[i] = max(dp1[i] + dp1[i-2], dp1[i-1])
    
    for i in range(2, len(stickers)):
        dp2[i] = max(dp2[i] + dp2[i-2], dp2[i-1])
    
    answer = max(dp1[-1], dp2[-1])
        
    return answer 
    