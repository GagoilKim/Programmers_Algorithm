def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    for i in range(len(new_id)):
        if new_id[i].isalnum() or new_id[i] in '-_.':
            answer+= new_id[i]
    while '..' in answer:
        answer = answer.replace("..", ".")
    if len(answer) > 1:
        if answer[0] == '.':
            answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1]
    if len(answer) == 0:
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[: -1]
    while len(answer) <= 2:
        answer += answer[len(answer) - 1]
    return answer