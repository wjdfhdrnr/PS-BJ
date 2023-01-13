import sys
Switch_num = int(sys.stdin.readline())
Switch_state = list(map(int,sys.stdin.readline().split()))
population = int(sys.stdin.readline())
student_information = []

for j in range(population):
    student_information.append(list(map(int,sys.stdin.readline().split())))

    if student_information[j][0]==1:#남자
            rotation = Switch_num//student_information[j][1]
            for k in range(1,rotation+1):
                Switch_state[(student_information[j][1]*k)-1] = int(not Switch_state[(student_information[j][1]*k)-1]) 
    else:#여자
        l=1
        while 1:
            if student_information[j][1] == 1 or student_information[j][1] == Switch_num:
                break
            else:
                if Switch_state[student_information[j][1]-1-l] == Switch_state[student_information[j][1]-1+l]:
                    Switch_state[student_information[j][1]-1-l] = int(not Switch_state[student_information[j][1]-1-l])
                    Switch_state[student_information[j][1]-1+l] = int(not Switch_state[student_information[j][1]-1+l])

                    if student_information[j][1]-l == 1 or student_information[j][1]+l == Switch_num:
                        break
                    else:
                        l+=1
                else:
                    break

        Switch_state[(student_information[j][1])-1] = int(not Switch_state[(student_information[j][1])-1])

for v in range(0,Switch_num,20):
    print(*Switch_state[v:v+20])
    
