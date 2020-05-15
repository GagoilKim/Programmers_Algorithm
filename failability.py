def solution(N, stages):
    answer = []
    pro = []
    numPlayer = len(stages)
    for i in range(N):
        count = 0
        for j in range(len(stages)):
            if i+1 == stages[j]:
                count+=1
        if numPlayer == 0:
            pro.append(0)
        else:
            pro.append(count/numPlayer)
            numPlayer-=count
    for x in range(N):
        tmp = pro.index(max(pro))
        answer.append(tmp+1)
        pro[tmp] = -1
    return answer