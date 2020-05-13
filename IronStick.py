def solution(arrangement):
    answer = 0
    bar = 0
    arrangement = arrangement.replace("()", "R")
    for x in arrangement:
        if x == "(":
            bar+=1
        elif x == ")":
            bar-=1
            answer+=1
        else:
            answer+=bar
    return answer