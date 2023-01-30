from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
paper = [list(map(int,input().strip().split())) for _ in range(n)]
check = [[False] * m for _ in range(n)]


dy = [0,1,0,-1]
dx = [1,0,-1,0]

def BFS(y,x):
    rs = 1
    q = deque()
    q.append((y, x))
    
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if paper[ny][nx]==1 and check[ny][nx]==False:
                    rs += 1
                    check[ny][nx]=True
                    q.append((ny,nx))
    return rs

maxv = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if paper[i][j] == 1 and check[i][j] == False:
            check[i][j] = True
            cnt +=1
            maxv = max(maxv,BFS(i,j))

print(cnt)
print(maxv)
