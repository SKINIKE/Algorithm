class Solution {
        fun solution(my_string: String): List<Int> {
        return my_string.toCharArray()
                .filter{ it.isDigit()}
                .sorted()
                .map{ Character.getNumericValue(it)}
    }
}