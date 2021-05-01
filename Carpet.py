def solution(brown, yellow):
    answer = []
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            tmp = yellow / i
            if (i + 2) * (tmp + 2) - (i * tmp) == brown:
                return [max(i + 2, tmp + 2), min(i + 2, tmp + 2)]