answer = 0
def solution(numbers, target):
    global answer 
    DFS(numbers, target, 0, 0)
    return answer

def DFS(numbers, target, length, value):
    l = len(numbers)
    global answer
    if length == l and target == value:
        answer+=1
        return
    if length == l:
        return
    DFS(numbers, target, length +1, value + numbers[length])
    DFS(numbers, target, length +1, value - numbers[length])