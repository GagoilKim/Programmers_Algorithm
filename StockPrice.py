from collections import deque 

def solution(prices):
    answer = []
    prices = deque(prices)
    while len(prices) :
        time = 0
        tmp = prices.popleft()
        for p in prices:
            time += 1
            if tmp > p:
                break
        answer.append(time)
    return answer