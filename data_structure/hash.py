'''
입력 = words
1. words의 두 요소가 *아나그램이면 True
2. 아나그램 : 요소가 같아 재배열만 하면 같은 문자를 만들 수 있는 것
출력 = T/F
'''
words = ["AbaAeCe", "baeeACA"]
result = []
answer = False

for word in words:
    dic = {}
    for alp in word:                        
        dic[alp] = dic.get(alp, 0) + 1      #dic에 요소가 없어도 추가하는 방법
    dic = sorted(dic.items())               
    result.append(dic)                      #result에 딕셔너리 추가

for i in range(len(result)):                #result의 요소가 같으면 True
    for j in range(i+1, len(result)):
        if result[i] == result[j]:
            answer = True

print(answer)