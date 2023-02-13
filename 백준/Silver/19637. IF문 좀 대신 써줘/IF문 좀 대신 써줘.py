import sys
input = sys.stdin.readline
N,M = map(int,input().split())
name = []
ran = []
user = []
for _ in range(N):
    a,b = input().split()
    name.append(a)
    ran.append(int(b))

for _ in range(M):
    user.append(int(input()))
#print(user)

def BinarySearch(st,en,target):
        #print("st=",st,"en=",en,"target=",target)
        mid = (st+en)//2
        
        if st == en:
            print(name[mid])
            
            return 

        if target > ran[mid]:
            BinarySearch(mid+1,en,target)
        
        else :
            BinarySearch(st,mid,target)


for target in user:

    BinarySearch(0,N-1,target)
