nums = [1,2,3,4,5,6,7,8]
def solution(nums):

    answer = []

    for num in nums:
        if num < 2:
            continue
        check = True
        for j in range(2, num // 2 + 1):
            if num % j == 0:
                check = False        
        if check:
            answer.append(num)
    
    print(answer)

solution(nums)
