'''
스택
- 리스트로 선언
- stack.append() 제일 뒤(-1)에 있는 요소 출력
- stack.pop()  제일 뒤(-1)에 요소 입력
'''

nums = [1,2,3,4,5,0,-1]
stack = []

'''
nums의 요소를 스택에 push 하다가
0이 나오면 pop()
-1이 나오면 종료
'''
for i in nums:
    if i == 0:
        stack.pop()
    elif i == -1:
        break
    else:
        stack.append(i)

print(stack)            # stack = [1, 2, 3, 4]