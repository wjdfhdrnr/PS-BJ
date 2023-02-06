N = int(input())

def counting_star(num):
    if num ==3:
        return ['***','* *','***']
    stars = counting_star(num//3)
    box = []    
    for s in stars:
        box.append(s*3)
    for s in stars:
        box.append(s+' '*(num//3)+s)
    for s in stars:
        box.append(s*3)
        
    return box
        

print(*counting_star(N),sep='\n')