def solution(progresses, speeds):
    answer = []
    count = []
    for x in range(0, len(progresses)):
        answer.append(1)
        i = 0
        while progresses[x] <=100:
            progresses[x] = progresses[x] + speeds[x]*1
            i = i+1
        count.append(i)
    
    for x in range(0, len(count)-1):
        if count[x] >count[x+1]:
            answer[x] = answer[x] +1
            del answer[x+1]
    
    return answer