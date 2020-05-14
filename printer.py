def solution(priorities, location):
    answer = 0
    large = max(priorities)
    size = len(priorities)
    target = priorities[location]
    for x in range(0, len(priorities)):
        maximum = max(priorities)
        while priorities.index(maximum) != 0:
            tmp = priorities[0]
            priorities.pop(0)
            priorities.append(tmp)
            print(priorities)
            answer+=1

        if priorities.index(target) ==  0:
            break;
        else:
            priorities.pop(0)

    if large == target:
            answer-=1
            return answer
    else:
        answer = size - answer+1
             
    return answer