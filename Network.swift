import Foundation

func solution(_ n:Int, _ computers:[[Int]]) -> Int {
    var visited = [Bool](repeating: false, count: n)
    var answer = 0
    
    for i in 0..<n {
        if visited[i] == false {
            answer += 1
            dfs(&visited, n, computers, i)
        }
    }
    return answer
}

func dfs(_ visited: inout [Bool], _ n: Int, _ computers: [[Int]], _ index: Int ) {
    visited[index] = true
    for i in 0..<n {
        if visited[i] == false && computers[index][i] == 1 {
            dfs(&visited, n, computers, i)
        }
    }
    
}