def solution(n, computers):
    answer = 0
    visited = [0]*n
    network = 1
    for i in range(n):
        DFS(i, visited, computers, n, network)
    
    answer = network
    print(visited[n-1])
    return answer

def DFS(idx, visited, computers, n, network):
    if idx == n:
        return
    if visited[idx] != 0:
        return
    visited[idx] = network
    for i in range(n):
        if visited[i] == 0 and computers[idx][i]:
            DFS(i, visited, computers, n, network)
        