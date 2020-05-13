def solution(arr, divisor):
    answer = []
    for x in range(0, len(arr)):
        result = arr[x]%divisor
        if result == 0:
            answer.append(arr[x])
    answer = sorted(answer)
    if len(answer) == 0:
        answer.append(-1)
    return answer