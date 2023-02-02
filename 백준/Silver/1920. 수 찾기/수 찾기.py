import sys 
input = sys.stdin.readline
N = int(input())
N_list = list(map(int,input().split()))
M = int(input())
M_list = list(map(int,input().split()))
N_list.sort()

def BinarySearch(st,en,target):
        mid = (st+en)//2
        
        if st == en:
            if N_list[mid] == target:
                print(1)
            else:
                print(0)
            return 

        if N_list[mid] < target:
            BinarySearch(mid+1,en,target)
        else :
            BinarySearch(st,mid,target)


for target in M_list:
    BinarySearch(0,N-1,target)
