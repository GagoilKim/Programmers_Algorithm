from collections import defaultdict

def solution(clothes):
    d = defaultdict(list)
    key = []
    for i in range(len(clothes)):
        d[clothes[i][1]].append(clothes[i][0])
        if clothes[i][1] not in key:
            key.append(clothes[i][1])
    print(key)
    print(len(d))
    answer = 0
    
    return answer