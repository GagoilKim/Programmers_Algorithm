def solution(s):
    answer = ''
    s = s.split(" ")
    
    for i in range(len(s)):
        s[i] = int(s[i])
    small = min(s)
    big = max(s)
    result = str(small) + " " + str(big)
    return result