def solution(bridge_length, weight, truck_weights):
    answer = 0
    b = bridge_length
    w = weight
    t = truck_weights
    time = 0
    q = [0] * b
    while q:
        time += 1
        q.pop(0)
        if t:
            if sum(q) + t[0] <= w:
                q.append(t.pop(0))
            else:
                q.append(0)
    return time