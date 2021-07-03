import Foundation

func solution(_ numbers:[Int]) -> [Int] {
    var result : [Int] = []
    for idx in 0 ..< numbers.count-1 {
        for jdx in idx + 1 ..< numbers.count {
            var sum = numbers[idx] + numbers[jdx]
            if result.contains(sum) == false {
                result.append(sum)
            }
        }
    }
    result = result.sorted()
    return result
}