import Foundation

func solution(_ w:Int, _ h:Int) -> Int64{
    var answer:Int64 = 0
    var total : Int = w * h
    var common : Int = 0
    for x in 1...w {
        if w % x == 0 && h % x == 0 {
            common = x
        }
    }
    let width = w / common
    let height = h / common
    let blocked = width + height - 1
    
    return Int64(total - (blocked) * common)
}