import UIKit

class Friend {

    func sayHi() {
        print("안녕")
    }
    
    class func sayBye() {
        print("하이")
    }
    
    static func sayhoho() { // final class 의미, 상속 X
        print("바이")
    }
}

let myFriend = Friend()
myFriend.sayHi()

Friend.sayBye()

Friend.sayhoho()
 
