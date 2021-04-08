from itertools import permutations

def solution(numbers):
    maximum = 0
    for num in permutations(numbers, len(numbers)):
        tmp = int(''.join([str(i) for i in num]))
        if tmp > maximum:
            maximum = tmp
            # print(maximum)
    
        
    return str(maximum)