#아이디어 
#DFS,2중 FOR문 배열 
#시간복잡도
#0(V+E) V = N*N  / E = 4*V = 5V 25*25*5  <2억
#자료구조
#DFS재귀함수, 2중 포문
import sys 
input = sys.stdin.readline
N = int(input())
area = [list(map(int,input().strip())) for _ in range(N)]
check = [[False] * N for _ in range(N)]
result =[]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def DFS(y,x):
    global each
    each +=1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<N and 0<=nx<N:
            if check[ny][nx] == False and area[ny][nx] == 1:
                check[ny][nx] = True
                DFS(ny,nx)



for i in range(N):
    for j in range(N):
        if area[i][j] == 1 and check[i][j] == False:
            check[i][j] = True
            each = 0
            DFS(i,j)
            result.append(each)

result.sort()
print(len(result)) 
for i in result:
    print(i)
