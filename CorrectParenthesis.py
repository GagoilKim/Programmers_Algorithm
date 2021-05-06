def solution(s):
    answer = True
    arr = []
    for i in range(len(s)):
        if s[i] == "(":
            arr.append("(")
        else:
            if len(arr) == 0:
                return False
            else:
                arr.pop()
    if len(arr) != 0:
        return False
    return True