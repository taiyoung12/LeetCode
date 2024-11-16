def solution(maps):
    row = len(maps)
    col = len(maps[0])
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    q = [[0,0]]
    
    while q:
        m = q.pop(0)
        x = m[0]
        y = m[1]
        
        if x == row-1 and  y == col-1:
            return maps[x][y]
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if -1 < nx < row and -1 < ny < col and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] +1
                q.append([nx, ny])
            
    return -1 