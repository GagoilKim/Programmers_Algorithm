def solution(numbers):
    answer = ''
    a = list(map(str, numbers))
    a.sort(key = lambda x:x*3, reverse=True)
    answer = int(''.join(a))
    return str(answer)