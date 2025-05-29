import UIKit

// 키: 값
var myFriends = ["bestFriend" : "친구1",
                 "highschool" : "친구2"
                ]

let myBestFriend = myFriends["bestFriend"] // 친구1
let highSchoolFriend = myFriends["highschool"] // 친구2
let youtubeFriend = myFriends["youtube" , default:"친구없음"] // 친구없음
