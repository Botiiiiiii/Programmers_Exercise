def solution(progresses, speeds):
    answer = []
    day_cnt = 0
    cnt = 1
    for data, time in zip(progresses, speeds):
        expect_time = int((100 - data) / time)
        if expect_time * time + data < 100: expect_time += 1
        # print("expect_time: ",expect_time)
        # print("day_cnt: ",day_cnt)
        if day_cnt >= expect_time:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            day_cnt = expect_time
    if cnt != 0:
        answer.append(cnt)

    return answer[1:]

print(solution([93, 30, 55], [1, 30, 5]))

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))