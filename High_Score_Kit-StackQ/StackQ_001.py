def solution(arr):
    answer = []
    top = 0
    for i in range(len(arr)):
        answer.append(arr[i])
        if i>0 and answer[top] == arr[i-1]:
            answer.pop()
            top -= 1
        top += 1

    return answer


print(solution([1,3,3,3,0,1]))

print(solution([0,0,0,0,1,1,0,3,3,0,1,1]))

print(solution([4,4,4,3,3]))