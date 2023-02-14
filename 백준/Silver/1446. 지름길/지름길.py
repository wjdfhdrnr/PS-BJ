import sys 
input = sys.stdin.readline
N,D = map(int,input().split())
graph = [list(map(int,input().rstrip().split())) for _ in range(N)]
Dis = [i for i in range(D+1)]
for i in range(D+1):
    Dis[i] = min(Dis[i],Dis[i-1]+1)
    for s,e,f in graph:
        if i == s and e <= D and Dis[i]+f <Dis[e]:
            Dis[e] = Dis[i]+f

print(Dis[D])
