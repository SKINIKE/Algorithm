class Solution {
    fun solution(numbers: IntArray): Int {
        val a = numbers.toList().sorted()[numbers.size-1] * numbers.toList().sorted()[numbers.size-2]
        val b = numbers.toList().sorted()[0] * numbers.toList().sorted()[1]
        
        return (if(a >= b) a else b)
    }
}