def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        binary1 = bin(arr1[i]).replace('0b', "")
        binary2 = bin(arr2[i]).replace('0b', "")
        if len(binary1) != n:
            binary1 = "0" * (n - len(binary1)) + binary1
        if len(binary2) != n:
            binary2 = "0" * (n - len(binary2)) + binary2
        tmp = ""
        for j in range(n):
            if binary1[j] != "1" and binary2[j] != "1":
                tmp+= " "
            else:
                tmp+= "#"
            print(tmp)
        answer.append(tmp)
    return answer