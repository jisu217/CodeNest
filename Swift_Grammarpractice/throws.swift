import UIKit

enum MismatchError: Error {
    case nameMismatch
    case numberMismatch
}

func guessMyName(name input: String) throws {
    print("guessMyName() called")
    
    if input != "홍길동" {
        print("틀렸다")
        throw MismatchError.nameMismatch // return
    }
    print("맞췄다")
}

try guessMyName(name: "사과")

// try?: 에러 처리를 하지 않을 경우 
// try!: 에러가 무조건 없을 것

do {
   try guessMyName(name: "이대리")
} catch {
    print("잡은 에러: \(error)")
}
