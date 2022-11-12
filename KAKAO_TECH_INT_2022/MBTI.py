def solution(survey, choices):
    from collections import defaultdict
    # R - T
    # C - F
    # J - M
    # A - N

    mbti_answer = [["R","T"],["C","F"],["J","M"],["A","N"]]

    mbti = defaultdict(int)

    answer = ""

    for data, score in zip(survey,choices):
        front = data[:1]
        back = data[1:]
        if score == 4:
            continue
        elif score > 4:
            mbti[back] += score - 4
        else:
            mbti[front] += 4 - score

    for data in mbti_answer:
        if mbti[data[0]] < mbti[data[1]]:
            answer += data[1]
        else:
            answer += data[0]

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))

print(solution(["TR", "RT", "TR"], [7, 1, 3]))