progresses = [93, 30, 55]
speeds = [1, 30, 5]

answer = []
time = 0
count = 0

while progresses:
    if (progresses[0] + time * speeds[0]) >= 100:   # 2. 100% 완료 되었으면 pop하고, count += 1
        progresses.pop(0)
        speeds.pop(0)
        count += 1

    else:
        time += 1                                   # 1. 100%완료 안됬으면 time += 1
        if count > 0:                               # 3. 이전에 완료된 기능이 있고, 현재꺼는 안됬으면
            answer.append(count)
            count = 0
answer.append(count)
print(answer)