class Solution {
    fun solution(my_string: String, num1: Int, num2: Int): String {
        var str = my_string.toMutableList()
        str[num2] = my_string.toList()[num1]
        str[num1] = my_string.toList()[num2]
        return str.joinToString("")
    }
}