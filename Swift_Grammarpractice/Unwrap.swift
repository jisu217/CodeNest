import UIKit

var someVariable : Int? = nil

if someVariable == nil {
    someVariable = 90
}

print("someVariable: ", someVariable)

if let otherVariable = someVariable {
    print("언래핑 되었다. 즉 값이 있다. otherVariable : \(otherVariable)")
} else {
    print("값이 없다.")
}

someVariable = nil

let myValue = someVariable ?? 10
print("myValue: \(myValue)")

var firstValue : Int? = 30
var secondValue : Int? = 50

print("firstValue: \(firstValue)")
print("secondValue: \(secondValue)")

unwrap(firstValue)
unwrap(secondValue)

func unwrap(_ parameter: Int?) {
    print("unwrap() called")

    guard let unWrappedParam = parameter else {
        return
    }
    print("unWrappedParam: \(unWrappedParam)")
}
