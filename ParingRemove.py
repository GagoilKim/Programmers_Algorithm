def solution(s):
    answer = 0
    result = []
    for i in (s):
        if len(result) == 0:
            result.append(i)
        elif result[-1] == i:
            result.pop(-1)
        else:
            result.append(i)
    if len(result) == 0:
        return 1
    else:
        return 0
