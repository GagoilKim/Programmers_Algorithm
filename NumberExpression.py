def solution(n):
    answer = 0
    for i in range(1, n):
        tmp = i
        add = i + 1
        while tmp < n:
            tmp += add
            add += 1
        if tmp == n:
            answer += 1
    answer += 1
    return answer