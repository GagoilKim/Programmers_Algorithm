import Foundation

func solution(_ numbers:[Int], _ hand:String) -> String {
    enum Side : String {
        case left = "L"
        case right = "R"
    }
    let leftNum = [1, 4, 7]
    let rightNum = [3, 6, 9]
    let others = [2, 5, 8, 0]
    
    var result : String = ""
    var currentHand : Side = .left
    var leftOn : Int = 10
    var rightOn : Int = 12
    
    
    for number in numbers {
        if leftNum.contains(number) {
            result += "L"
            leftOn = number
        } else if rightNum.contains(number) {
            result += "R"
            rightOn = number
        } else {
            var target = number
            if number == 0 {
                target = 11
            }
            var leftNow = leftOn
            var rightNow = rightOn
            var leftDis = abs(target - leftNow)
            var rightDis = abs(target - rightNow)
            leftDis = (leftDis / 3) + (leftDis % 3)
            rightDis = (rightDis / 3) + (rightDis % 3)
             if leftDis < rightDis {
                leftOn = target
                result += "L"
                } else if leftDis > rightDis {
                rightOn = target
                result += "R"
                } else {
                if hand == "right" {
                    rightOn = target
                    result += "R"
                } else {
                    leftOn = target
                    result += "L"
                }
                
            
            }
        }
    }
    print(result)
    
    return result
}