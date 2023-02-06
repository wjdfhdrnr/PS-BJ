
import sys
input = sys.stdin.readline
N,M = map(int,sys.stdin.readline().split())
MAX_VAL =100*1000+1
load = []
for _ in range(N):
    load.append(list(map(int,(input().strip().split()))))

dp = [[[MAX_VAL]*3 for _ in range(M)] for _ in range(N)]

for y in range(N):
    if y == 0:
        for x in range(M):
            for d in range(3):
                dp[y][x][d] = load[y][x]
    else:
        for x in range(M):
            if x == 0 :
                    dp[y][x][0] = min(dp[y-1][x+1][1]+load[y][x],dp[y-1][x+1][2]+load[y][x])
                    dp[y][x][1] = dp[y-1][x][0]+load[y][x]
            elif x == M-1:
                    dp[y][x][1] = dp[y-1][x][2]+load[y][x]
                    dp[y][x][2] = min(dp[y-1][x-1][0]+load[y][x],dp[y-1][x-1][1]+load[y][x])
            else:
                dp[y][x][0] = min(dp[y-1][x+1][1]+load[y][x],dp[y-1][x+1][2]+load[y][x])
                dp[y][x][1] = min(dp[y-1][x][0]+load[y][x],dp[y-1][x][2]+load[y][x])
                dp[y][x][2] = min(dp[y-1][x-1][0]+load[y][x],dp[y-1][x-1][1]+load[y][x])
result = 1e9

for x in range(M):
    result = min(min(dp[N-1][x]),result)
print(result)
