N,G = input().split()
N = int(N)
player = []
for i in range(N):
    i = input()
    player.append(i)

player = set(player)
real_num = len(player)


if G =="Y":
    print(real_num)
elif G =="F":
    print(real_num//2)
elif G =="O":
    print(real_num//3)