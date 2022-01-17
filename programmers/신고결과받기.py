from itertools import zip_longest


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
# result = [2,2,1,0]
'''id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3'''

def solution(id_list, report, k):
    answer = [0] * len(id_list)                 # [0, 0, 0, ...]
    dic = {id: [] for id in id_list}            
    
    for x in set(report):                       # set 중복신고제거
        x = x.split(' ')                        # 피신고자 : 신고자, 신고자 ...
        dic[x[1]].append(x[0])                  

    for key, value in dic.items():              
        if len(value) >= k:
            for v in value:
                answer[id_list.index(v)] += 1

    return answer

print(solution(id_list, report, k))