import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
num_list = list(map(int,input().split()))
op = list(map(int,input().split()))
rs = num_list[0]
maxv = -int(1e9)
minv = int(1e9)

def backtracking(num,rs,a,b,c,d):
    global maxv , minv
    if num == N-1:
        maxv= max(maxv,rs)
        minv= min(minv,rs)
        return

    if a > 0:
        backtracking(num+1,rs+num_list[num+1],a-1,b,c,d)
    if b > 0:
        backtracking(num+1,rs-num_list[num+1],a,b-1,c,d)
    if c > 0:
        backtracking(num+1,rs*num_list[num+1],a,b,c-1,d)
    if d > 0:
        backtracking(num+1,int(rs/num_list[num+1]),a,b,c,d-1)
    

backtracking(0,num_list[0],op[0],op[1],op[2],op[3])
print(maxv)
print(minv)