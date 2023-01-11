text =""
m_text = 'aeiou'
while 1:
    text = input()
    sum = 0
    end_point = 0
    if text == 'end':
        break

    for i in range(len(text)):
        
        #첫 if문 모음이 포함 돼 있는지 ? 모음 개수 count
        if text[i] in m_text:  
            sum +=1           

        #같은 글자 두번 오는 거 check
        if i > 0:
            if text[i] == text[i-1]:
                if text[i] =='o' and text[i-1] == 'o':
                    next
                elif text[i] =='e' and text[i-1] == 'e':
                    next
                else:
                    end_point=1
                    break

        #모음3개 혹은 자음3개
        if i >1:
            if text[i] in m_text:
                if text[i-1] in m_text:
                    if text[i-2] in m_text:       
                        end_point=1
                        break                      
            else:
                if text[i-1] not in m_text:
                    if text[i-2] not in m_text:             
                            end_point=1
                            break  
               
    if sum != 0 and end_point == 0:
        print("<"+text+"> is acceptable.")
    elif end_point !=0:
        print("<"+text+"> is not acceptable.")
    else :
        print("<"+text+"> is not acceptable.")