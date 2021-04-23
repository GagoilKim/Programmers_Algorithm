def solution(n):
    answer = n
    ones = bin(n).count('1')
    newOnes = 0
    while(ones != newOnes):
        answer += 1
        newOnes = bin(answer).count('1')
    return answer