def solution(priorities, location):
    answer = 0
    count = 0
    pick = location
    while len(priorities) != 0:
        m = max(priorities)
        if pick == 0:
            if m == priorities[pick]:
                count += 1
                return count
            else:
                tmp = priorities.pop(0)
                priorities.append(tmp)
                pick = len(priorities)-1
        else:
            tmp = priorities.pop(0)
            if m == tmp :
                count += 1
            else:
                priorities.append(tmp)
            pick -= 1
                

    return count