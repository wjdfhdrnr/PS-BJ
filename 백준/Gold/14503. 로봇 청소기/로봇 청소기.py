import sys
N,M = map(int,input().split())
r,c,d = map(int,input().split())
area = [list(map(int,input().strip().split())) for _ in range(N)]
#북동남서//0123
dy = [-1,0,1,0]
dx = [0,1,0,-1]
y,x =[r,c]
switch = True
cnt = 0
#회전
while switch:
    point = area[y][x]
    # print(y,x,d,"while문 맨 앞")
#1.현재위치를 청소한다
    if point != 1:
        if point == 0:
            area[y][x] = 2
            cnt +=1
            # print('청소해요')
            # input()

#2.현재 방향을 기준으로 왼쪽방향부터 탐색을 진행한다
        for _ in range(4):
            if d==0:
                d+=3
                # print('포문속+3',d)
                # input()
            else :
                d-=1
                # print('포문속-1',d)
                # input()

            y = y + dy[d]
            x = x + dx[d] 
            
#2-1~4.왼쪽 방향에 청소하지 않은 공간이 존재, 그 방향으로 회전 한칸 전진 다시 1번
            if area[y][x] == 0:
                # print(y,x,d)
                # input()
                break
                
            else:
                y = y - dy[d]
                x = x - dx[d]
                # print(y,x,d)
                # input()
#4방향 다 못 찾았을 때
        #후진 안됨
        if area[y][x] != 0 and area[y-dy[d]][x-dx[d]] == 1 :
            switch = False
        #후진시켜
        elif area[y][x] == 2 and area[y-dy[d]][x-dx[d]] == 2 :
            y = y - dy[d]
            x = x - dx[d] 


print(cnt)