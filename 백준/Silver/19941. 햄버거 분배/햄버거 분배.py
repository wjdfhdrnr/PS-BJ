import sys 
N,K = map(int,sys.stdin.readline().split())
array = list(sys.stdin.readline())
food = []
sum = 0
for i in range(N):
    if array[i] == 'H':
        food.insert(i,'1')
    else :
        food.insert(i,'0')

for j in range(N):
    if food[j] == '0':
        for n in range(-K,K+1):           
            if j+n<0 or j+n>N-1:
                next
            else:
                if food[j+n] == '1':
                    food[j+n] = '-1'
                    sum +=1
                    break
       
print(sum)
