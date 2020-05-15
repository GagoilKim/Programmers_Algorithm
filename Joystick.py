def solution(name):
    answer = 0
    arr = []

    for i in range(len(name)):
            dif = abs(ord("A") - ord(name[i]))
            arr.append(dif)
    print(arr)
    cur = 0
    for i in range(len(arr)):
        answer += arr[cur]+1
        print(cur)
        if arr[cur-1] < arr[cur+1]:
            cur = cur-1
        else:
            cur = cur+1
    return answer