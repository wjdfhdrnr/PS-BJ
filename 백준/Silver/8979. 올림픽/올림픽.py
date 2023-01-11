import sys
N,K = map(int,(input().split()))
grade = []

for i in range(N):
    grade.append(list(map(int,input().split())))

seqence = [1 for i in range(N)]

for j in range(N):
    if grade[j][0] == K:
        answer = j
    for k in range(4):
        if grade[j][1] < grade[k][1]:
            seqence[j] +=1
        elif grade[j][1] == grade[k][1]:
            if grade[j][2] < grade[k][2]:
                seqence[j] +=1
            elif grade[j][2] == grade[k][2]:
                if grade[j][3] < grade[k][3]:
                    seqence[j] +=1
# print(seqence)
print(seqence[answer])