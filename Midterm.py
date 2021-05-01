def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    oCount = 0
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    tCount = 0
    thr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    thCount = 0
    while len(answers) > 0:
        cur = answers[0]
        o = one.pop(0)
        one.append(o)
        if o == cur:
            oCount += 1
        t = two.pop(0)
        two.append(t)
        if t == cur:
            tCount += 1
        tc = thr.pop(0)
        thr.append(tc)
        if tc == cur:
            thCount += 1
            
        answers.pop(0)
    
    m = max(oCount, tCount, thCount)
    if m == oCount:
        answer.append(1)
    if m == tCount:
        answer.append(2)
    if m == thCount:
        answer.append(3)
        
    return answer