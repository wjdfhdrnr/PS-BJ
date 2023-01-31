import sys
input = sys.stdin.readline

N,M = map(int,input().split())
rs = []
check = [False] * (N+1)

def recursion(num):
    if num == M:
        print(" ".join(map(str, rs)))
        return
    for i in range(1,N+1):
        if check[i] == False:
            check[i] = True
            rs.append(i)
            
            recursion(num+1)
            check[i] = False
            rs.pop()
            

recursion(0)
    