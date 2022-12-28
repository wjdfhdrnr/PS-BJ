import sys
M = int(sys.stdin.readline())
S = set()

for _ in range(M):
    text = sys.stdin.readline().strip()
    if text == "all":
        S = set(range(1,21))
    elif text == "empty":
        S.clear()
    else:
        text,x=text.split()    
        x = int(x)

    if text == "add":
        if x not in S:
            S.add(x)          

    elif text == "check":
        if x in S:
            print(1)
        else:
            print(0)

    elif text == "remove":
        if x in S:
            S.remove(x)

    elif text == "toggle":
        if x in S:
            S.remove(x)
        else :
            S.add(x)
        