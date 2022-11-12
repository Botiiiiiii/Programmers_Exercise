def solution(sizes):
    answer = 0
    max_x = 0
    max_y = 0
    for x, y in sizes:
        if x < y:
            tmp = x
            x = y
            y = tmp
        if max_x < x:
            max_x = x
        if max_y < y:
            max_y = y
    return max_x * max_y

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
