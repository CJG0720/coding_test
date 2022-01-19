'''
clothes = [item, category]
아이템을 사용하여 위장 가능한 경우의 수 return

'''
clothes = [["yellowhat", "headgear"], 
["bluesunglasses", "eyewear"], 
["green_turban", "headgear"]]

def solution(clothes):
    cnt = 1
    dict = {}

    for item in clothes:
        if item[1] in dict  : dict[item[1]] += 1
        else                : dict[item[1]] = 1

    for i in dict.values():                             # [2, 1] (headgear랑 eyewear)
        cnt *= (i+1)                                    
    return cnt -1                                       # 전부 안 입는 경우는 없음

print(solution(clothes))