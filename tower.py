def solution(heights):
    answer = []
    for i in range(0, len(heights)):
        tmp = heights.pop()
        bef = len(answer)
        for j in range(0, len(heights)):
            ind = len(heights)-j-1
            if heights[ind]> tmp:
                answer.append(ind+1)
                break
        if bef == len(answer):
            answer.append(0)
    last = []
    for i in range(0, len(answer)):
        last.append(answer.pop())
    return last