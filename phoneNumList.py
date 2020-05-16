import re
def solution(phone_book):
    answer = True
    minlen = len(phone_book[0])
    ind = 0
    for i in range(1, len(phone_book)):
        if len(phone_book[i]) < minlen:
            minlen = len(phone_book[i])
            ind = i
    tmp = phone_book[ind]
    phone_book[ind] = '000'
    for j in range(len(phone_book)):
        front = re.findall("." * minlen, phone_book[j])
        if front[0] == tmp:
            answer = False
    return answer