import sys
from collections import deque
N = int(sys.stdin.readline())

card = deque(range(1,N+1))

for i in range(N-1):
    card.remove(card[0])
    down = card.popleft()
    card.append(down)

print(card[0]) 