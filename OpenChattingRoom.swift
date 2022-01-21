import Foundation

func solution(_ record:[String]) -> [String] {
    var result : [String] = []
    var user : [String : String] = [:]
    for rec in record {
        let splitted = rec.components(separatedBy: " ")
        if splitted[0] == "Enter" || splitted[0] == "Change" {
            user[splitted[1]] = splitted[2]
        }
    }
    for rec in record {
        let splitted = rec.components(separatedBy: " ")
        if splitted[0] == "Enter" {
            let txt = user[splitted[1]]! + "님이 들어왔습니다."
            result.append(txt)
        } else if splitted[0] == "Leave" {
            let txt = user[splitted[1]]! + "님이 나갔습니다."
            result.append(txt)
        }
    }
    return result
}