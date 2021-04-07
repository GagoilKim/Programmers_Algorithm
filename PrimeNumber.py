from itertools import permutations

def solution(numbers):
    answer = 0
    numlist = []
    for i in range(1, len(numbers) + 1):
        for num in permutations(numbers, i):
            tmp = int("".join(num))
            check = True

            if tmp > 1:
                if tmp not in numlist:
                    numlist.append(tmp)
                    for j in range(2, tmp ):
                        if tmp % j == 0:
                            check = False
                            break
                    if check == True:
                        print(tmp)
                        answer += 1

    return answer