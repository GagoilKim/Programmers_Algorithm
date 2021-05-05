def solution(s):
    answer = []
    # s = s.split(",{")
    s = s[2: -2]
    s = sorted(s.split("},{"), key = lambda x: len(x))

    for i in range(len(s)):
        tmp = s[i].split(",")
        for j in range(len(tmp)):
            if int(tmp[j]) not in answer:
                answer.append(int(tmp[j]))
    return answer