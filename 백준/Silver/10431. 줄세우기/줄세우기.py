P = int(input())
test = []
rotation = 0

while rotation!=P:
    sum = 0
    rotation+=1
    test = list(map(int,input().split()))
    number = test.pop(0)

    for i in range(1,20):
        
        for j in range(i):
            
            if test[i]<test[j]:
                    # print(test[i],test[j])
                test.insert(j,test[i])                        
                del test[i+1]             
                sum+= i-j

    print(number,sum)   
