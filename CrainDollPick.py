def solution(board, moves):
    answer = 0
    l = []
    for i in range(len(moves)):
        pick = moves[i]
        for j in range(len(board)):
            tmp = board[j][pick - 1]
            if tmp != 0:
                l.append(tmp)
                board[j][pick - 1] = 0
                break
    while l:
        prev = 0
        print(l)
        for i in range(len(l)):
            if l[i] == prev:
                answer += 2
                l.pop(i)
                l.pop(i - 1)
                print(prev)
                prev = 0
                break
            prev = l[i]
            if i == len(l) - 1:
                return answer
    return answer

