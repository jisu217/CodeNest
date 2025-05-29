import UIKit

var myArray : [Int] = [0,1,2,3,4,5,6,7,8,9,10]

for item in myArray {
    print("item: \(item)")
}

for item in myArray where item > 5 { // where 조건을 넣음
    print("5보다 큰수: \(item)")
}
