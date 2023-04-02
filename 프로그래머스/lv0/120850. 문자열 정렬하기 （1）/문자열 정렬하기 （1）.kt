class Solution {
    fun solution(myString: String) = myString.replace("[A-Z|a-z]".toRegex(), "")
        .toList()
        .sorted()
        .map { it.toString().toInt() }
        .toIntArray()
}