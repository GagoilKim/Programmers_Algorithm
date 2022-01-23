import Foundation

func solution(_ clothes:[[String]]) -> Int {
    var dic : [String : Int] = [:]
    for clothe in clothes {
        if dic[clothe[1]] != nil {
            dic[clothe[1]]! += 1
        } else {
            dic[clothe[1]] = 1
        }
    }
    var answer = 1
    dic.keys.forEach{ answer *= (dic[$0]! + 1) }
    return answer - 1
}