import Foundation

func solution(_ lottos:[Int], _ win_nums:[Int]) -> [Int] {
    var same : Int = 0
    var zero : Int = 0
    for (index, element) in lottos.enumerated() {
        if lottos.contains(win_nums[index]) {
            same += 1
        } 
        if lottos[index] == 0 {
            zero += 1
        }
    }
    var high = 7 - (zero + same)
    if high == 7 {
        high = 6
    }
    var low = 7 - same
    if low == 7 {
        low = 6
    }   
    return [high, low ]
}