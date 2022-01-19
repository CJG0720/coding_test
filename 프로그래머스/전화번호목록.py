phone_book = ["119", "97674223", "1195524421"]  # false
#phone_book = ["123","456","789"]                # True


def solution(phone_book):
    answer = True
    dic = {}

    for p in phone_book:
        dic[p] = 1
    for p in phone_book:
        temp = ""
        for num in p:
            temp += num
            print(temp, p)
            if temp in dic and temp != p:
                return False
    return answer

print(solution(phone_book))