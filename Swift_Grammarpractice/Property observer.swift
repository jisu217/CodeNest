import UIKit

var myAge = 0 {
    willSet{
        print("값이 생성될 예정이다. myAge: \(myAge)")
    }
    
    didSet{
        print("값이 설정되었다. myAge: \(myAge)")
    }
}

myAge = 10

// 값이 생성될 예정이다. myAge: 0
// 값이 생성되었다. myAge: 10

myAge = 20

// 값이 생성될 예정이다. myAge: 10
// 값이 생성되었다. myAge: 20
