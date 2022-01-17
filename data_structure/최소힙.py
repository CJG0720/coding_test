import heapq as hq

'''
   자연수는 최소힙에 입력한다
 0 최소힙에서 최솟값을 꺼내어 출력
-1 프로그램 종료
'''

nums = [5, 3, 6, 0, 5, 0, 2, 4, 0, -1]
a = []

'''for num in nums:
    if num == -1:
        break
    elif num == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))    #root를 pop
    else:
        hq.heappush(a, num)
'''