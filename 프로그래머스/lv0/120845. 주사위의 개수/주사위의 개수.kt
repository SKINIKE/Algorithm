class Solution {
    fun solution(box: IntArray, n: Int): Int {
        var answer = 1
        for(i in box.indices){
            answer *= box.map{it/n}[i]
        }
        return answer
    }
}