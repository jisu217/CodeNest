import UIKit

for index in 0...5 { // 0,1,2,3,4,5
    print("호호 index: \(index)")
}

for index in 0..<5 { // 0,1,2,3,4
    print("호호 index: \(index)")
}

for index in 0..<5 where index % 2 == 0 {
    print("호호 짝수 index: \(index)")
