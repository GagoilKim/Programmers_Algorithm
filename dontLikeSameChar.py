def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    tmp = 10
    for x in range(0, len(arr)):
        if tmp != arr[x]:
            answer.append(arr[x])
            tmp = arr[x]        
    print('Hello Python')
    return answer