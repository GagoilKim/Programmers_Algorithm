def solution(n):
    answer = ''
    l = ["1", "2", "4"]
    while n > 0:
        n -= 1
        k = n % 3
        answer = l[k] + answer
        n //= 3
        
    return answer