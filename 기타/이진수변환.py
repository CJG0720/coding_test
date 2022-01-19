'''
<문제>
1. 10진수 N이 입력되면 2진수로 변환하여 출력하기
2. 재귀함수 사용하기
<답>
1011
'''
N = 11
answer = []

def solution(N):
    if N == 0:
        return
    else:
        solution(N//2)
        answer.append(N % 2)        #재귀부분 밑에 있으면 역순으로 출력됨
                                    #D(11) / D(5) / D(2) / D(1)/ D(0)
                                    #조건이 종료되면 스택 출력
solution(N)
print(answer)
