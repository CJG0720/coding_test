def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n          # 최악의 소요시간 : 60   
    
    while left < right:             # while 1 < 60
        mid = (left + right) // 2   # mid = 30, 15, 23, 27, 29, 28
        total = 0                   
        for t in times:
            total += mid // t
  
        if total >= n:
            right = mid
        else:
            left = mid + 1
    
    answer = left
    return answer

n = 6
times = [7, 10]
print(solution(n, times))