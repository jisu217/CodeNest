import UIit

func myFunction(name: String) → String{
    return "안녕하세요?! \(name) 입니다!"
}

myFunction(name: "스위프트")
// 안녕하세요?! 스위프트 입니다

func myFunctionSecond(with name: String) → String{
    return "안녕하세요?! \(name) 입니다!"
}

myFunctionSecond(with: "Swift")
// 안녕하세요?! Swift 입니다
    
func myFunctionThird(_ name: String) → String{
    return "안녕하세요?! \(name) 입니다!"
}

myFunctionSecond(with: "스위프트")
// 안녕하세요?! 스위프트 입니다
