import sys 
input = sys.stdin.readline
N,d,k,c = map(int,input().split())
belt = [(input().strip()) for _ in range(N)]
dish = []
rs = 1
# 이어주기
for i in range(k-1):
    belt.append(belt[i])
#쿠폰번호 초밥이 회전대에 포함 돼 있는 경우
if str(c) in belt:
    idx = belt.index(str(c))
    #print(idx)

    for i in range(k):
        if belt[i] != belt[idx]:
            if belt[i] not in dish:
                rs += 1
            dish.append(belt[i])
        else:
            dish.append(belt[i])
        #print("dish=",dish,"rs=",rs)
    maxv = rs

    for i in range(k,len(belt)):
        if belt[i] != belt[idx]:
            if belt[i] not in dish:
                rs +=1
            dish.append(belt[i])
        else:
            dish.append(belt[i])
        chk = dish.pop(0)
        if chk != belt[idx]:
            if chk not in dish :
                rs -=1
        #print("dish=",dish,"rs=",rs)
        maxv = max(maxv,rs)
else:#쿠폰번호 초밥이 회전대에 포함 안돼있는 경우
    for i in range(k):
        if belt[i] not in dish:
                rs += 1
        dish.append(belt[i])
        #print("dish=",dish,"rs=",rs)
    maxv = rs
       
    for i in range(k,len(belt)):
        
        if belt[i] not in dish:
            rs +=1
        dish.append(belt[i])
        chk = dish.pop(0)
        if chk not in dish :
            rs -=1
        maxv = max(maxv,rs)
        #print("dish=",dish,"rs=",rs)
print(maxv)