import Foundation

let line = readLine()!
let lineArr = line.components(separatedBy: " ")
let a = Int(lineArr[0])!
let b = Int(lineArr[1])!

var c = "=="

if  a > b
{
    c = ">"
}
else if a < b
{
    c = "<"
}

print(c)