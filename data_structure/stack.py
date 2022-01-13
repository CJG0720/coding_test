'''
후위표기식을 스택으로 연산
'''

num = '352+*9-'
operator = ['+', '-', '*', '/']

def postifx(num):
    stack = []
    for i in num:
        if i.isdecimal() == True:               # 0~9 == isdecimal() == True 
            stack.append(int(i))
        else:
            if i == '+':                        #operator
                x, y = stack.pop(), stack.pop()
                stack.append(x+y)
            elif i == '-':
                x, y = stack.pop(), stack.pop()
                stack.append(-(x-y))
            elif i == '/':
                x, y = stack.pop(), stack.pop()
                stack.append(x/y)            
            elif i == '*':
                x, y = stack.pop(), stack.pop()
                stack.append(x*y)
    return stack

print(postifx(num))                             # 12