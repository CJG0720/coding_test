from collections import deque
n = 8
k = 3

deq = deque([i+1 for i in range(n)])    

while deq:
    for _ in range(k-1):
        cur = deq.popleft()     # 빼고
        deq.append(cur)         # 넣고
    deq.popleft()               # 3번째는 제거
    if len(deq) == 1:           # 1개만 남으면
        print(deq[-1])          # 7
