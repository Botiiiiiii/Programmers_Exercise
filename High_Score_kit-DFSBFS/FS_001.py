def solution(numbers, target):
    res = [0]
    def dfs(i, summ):
        if i == len(numbers):
            if summ == target:
                res[0] += 1
            return

        dfs(i + 1, summ + numbers[i])
        dfs(i + 1, summ - numbers[i])

    dfs(0, 0)

    return res[0]


print(solution([1,1,1,1,1],3))
print(solution([4,1,2,1],4))