
import sys
input = sys.stdin.readline
N,K = map(int,input().split())
temp = list(map(int,input().split())) 
maxvv = 0


for i in range(K):
    maxvv += temp[i]
maxv = maxvv

for i in range(K,N):
    maxvv += temp[i]
    maxvv -= temp[i-K]
    maxv = max(maxv,maxvv) 
print(maxv)
