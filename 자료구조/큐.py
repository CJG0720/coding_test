'''
큐
- deque() 로 선언
- dq.popleft()  왼쪽에서 큐 요소 출력
- dq.append()   오른쪽으로 큐 요소 입력

'''

from collections import deque

nums = [1,2,3,4,5,0,-1]
dq = deque()

'''
nums의 요소를 스택에 push 하다가
0이 나오면 popleft()
-1이 나오면 종료
'''
for i in nums:
    if i == 0:
        dq.popleft()
    elif i == -1:
        break
    else:
        dq.append(i)

print(dq)            # dq = [2, 3, 4, 5]