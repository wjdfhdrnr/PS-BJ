import sys
N,Score,P = map(int,sys.stdin.readline().split())
rank = list(map(int,sys.stdin.readline().split()))
grade = 1
if N!=0: 
        
    if N==P and Score <= min(rank):
        grade = -1 
    else:
        for i in range(N):  
            if Score < rank[i]:
                grade +=1
else:
    grade=1       
print(grade)
