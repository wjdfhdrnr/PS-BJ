import sys
input = sys.stdin.readline
array = input().strip()
cnt = 0
for i in range(2):
    cnt = int(array.count(f"{i}"))
    for _ in range(int(cnt/2)):
        print(i,end="")

        