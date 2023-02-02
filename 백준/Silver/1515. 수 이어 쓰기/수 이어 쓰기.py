import sys
# i = 0
# maxv =input()
# while maxv !="":
#     for _ in range(4):
#         input()
#         print(maxv)
#         maxv = maxv[1:] 

input = sys.stdin.readline
maxv = input().strip()
i = 0

while maxv != "":
    i+=1

    num = str(i)
    for j in range(len(num)):
        if num[j] == maxv[0]:
            maxv = maxv[1:]
        if  maxv == "" :
            print(i)
            break