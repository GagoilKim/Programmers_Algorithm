import Foundation

func solution(_ begin:String, _ target:String, _ words:[String]) -> Int {
    var queue : [String] = []
    queue.append(begin)
    
    var check = [Bool](repeating: false, count: words.count)
    var count = 0
    
    if !words.contains(target) {
        return count
    }
 
    while !queue.isEmpty {
        let word = queue.popLast()!
        if word == target {
            break
        }
        count += 1
        print(count)
        for index in 0..<words.count {
            if !check[index] {
                if checkWord(word, words[index]) {
                    queue.append(words[index])
                    print(queue)

                    check[index] = true
                }
            }
        }
    }
    
    return count
}

func checkWord(_ word: String, _ target : String) -> Bool {
    var count = 0
    let wordMap = Array(word)
    let targetMap = Array(target)
    for index in 0..<wordMap.count {
        if wordMap[index] == targetMap[index] {
            count += 1
        }
    }
    return count == 1 ? true : false
}