def solution(priorities, location):
    rank_data = [x for x in range(len(priorities))]
    rank = 0
    while (len(priorities) > 1):
        data = priorities.pop(0)
        data_r = rank_data.pop(0)
        if data >= max(priorities):
            if data_r == location:
                return rank+1
            rank += 1
        else:
            priorities.append(data)
            rank_data.append(data_r)
    return rank + 1




print(solution([2,1,3,2],2))

print(solution([1,1,9,1,1,1],0))