N = int(input())
matchup = []
for i in range(N):
    x,y = map(int,input().split())
    matchup.append((x,y))

grade = [0 for i in range(N)]

for i in range(N):
    k=1
    for j in range(N):
        if matchup[i][0] < matchup[j][0] and matchup[i][1] < matchup[j][1]:
            k+=1
    grade[i] =k 
for z in range(N):
    print(grade[z],end=" ")