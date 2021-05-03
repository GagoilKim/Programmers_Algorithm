def solution(phone_book):
    answer = True
    array = phone_book
    array.sort()
    for i in range(len(array) - 1):
        tmp = array[i]
        if tmp in array[i + 1]:
            answer =  False
            break
    return answer