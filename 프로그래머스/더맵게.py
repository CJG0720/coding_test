'''
섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + 
(두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

'''
import heapq as hq

scoville = [2,3,7,10,15]
K = 7

def solution(scoville, K):
    hq.heapify(scoville)
    answer = 0

    while scoville[0] < K:
        if len(scoville) > 1:
            answer += 1
            hq.heappush(scoville, hq.heappop(scoville)+hq.heappop(scoville)*2)
        else:
            return -1
    return answer

print(solution(scoville, K))