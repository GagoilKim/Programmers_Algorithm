def solution(s):
    answer = ''
    s = s.split(" ")
    for i in range(len(s)):
        # s[i] = (s[i][0].upper() + s[i][1:].lower())
        s[i] = s[i].capitalize()
    answer = " ".join(s)
    return answer