def solution(dartResult):
    answer = 0
    arr = []
    for i in range(len(dartResult)):
        tmp = ""
        if dartResult[i].isnumeric():
            if dartResult[i+1] == "S":
                tmp = int(dartResult[i])
            elif dartResult[i+1] == "D":
                tmp = pow(int(dartResult[i]), 2)
            elif dartResult[i+1] == "T":
                tmp = pow(int(dartResult[i]), 3)
            arr.append(tmp)
            print(arr)

    return answer