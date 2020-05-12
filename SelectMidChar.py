def solution(s):
    answer = ""
    length =int(len(s))
    if length%2 == 0:
        answer = s[int(length/2)-1: int((length/2) +1)]
    else:
        answer = s[int(length/2)]
    return answer