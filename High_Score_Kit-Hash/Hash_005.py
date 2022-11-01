def solution(genres, plays):
    answer = []
    from collections import defaultdict
    s = defaultdict(dict)
    s_num = defaultdict(int)
    for x, (idx, cnt) in zip(genres, enumerate(plays)):
        s[x][idx] = cnt
        s_num[x] += cnt

    s_num = dict(sorted(s_num.items(), key=lambda item:item[1], reverse= True))

    for x in s_num:
        tmp_dict = (dict(sorted(s[x].items(),key= lambda item: item[1],reverse = True)))
        answer.extend(list(tmp_dict.keys())[:2])
    return answer

solution(["classic", "pop", "test", "classic", "pop", "test2"], [500, 500, 400, 600, 500,700])

