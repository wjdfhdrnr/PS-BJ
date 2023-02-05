import sys
input = sys.stdin.readline
N = int(input())

rs = [0,1,2]

for i in range(3, N+1):
    rs.append(rs[i-1]+rs[i-2])

print(rs[N]%10007)