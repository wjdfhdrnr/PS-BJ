import sys
from collections import deque
input = sys.stdin.readline
N,M,V =map(int,input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
check_DFS = [0*(N+1) for _ in range(N+1)]
check_BFS = [0*(N+1) for _ in range(N+1)]

def BFS(V):
    q = deque()
    q.append(V)
    check_BFS[V] = 1
    while q:
        V = q.popleft()
        print(V,end = " ")
        for j in range(1,N+1):
            if check_BFS[j] != 1 and graph[V][j] ==1:
                q.append(j)
                check_BFS[j] = 1


def DFS(V):
    check_DFS[V] = 1
    print(V,end = " ")
    for k in range(1,N+1):
        if check_DFS[k] != 1 and graph[V][k] ==1:
            DFS(k)


for i in range(M):
    a,b = map(int,input().strip().split())
    graph[a][b] = 1
    graph[b][a] = 1

DFS(V)
print()
BFS(V)

