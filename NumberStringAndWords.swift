import Foundation

func solution(_ s:String) -> Int {
    enum Words : String {
    case zero
    case one
    case two
    case three
    case four
    case five
    case six
    case seven
    case eight
    case nine
    
    var toString: Int {
        switch self{
        case .zero:
            return  0
        case .one :
            return 1
        case .two :
            return 2
        case .three:
            return 3
        case .four:
            return 4
        case .five:
            return 5
        case .six:
            return 6
        case .seven:
            return 7
        case .eight:
            return 8
        case .nine:
            return 9
        }
    }
}
    var result = ""
    var now = ""
    for char in s {
        var current = Int(String(char))
        if current != nil {
            result += String(current!)
        } else {
            now += String(char)
            var word = Words(rawValue: now)
            if let real = word {
                result += String(real.toString)
                now = ""
            }
        }
        
    }
    if let number = Int(result) {
        return number
    } else {
        return 0
    }
}