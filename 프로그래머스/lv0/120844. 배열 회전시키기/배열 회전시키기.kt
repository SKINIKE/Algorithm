import java.util.Collections

class Solution {
    fun solution(numbers: IntArray, direction: String): IntArray {
        val list = numbers.toList()
        if(direction == "right"){
            Collections.rotate(list, 1);
        }
        else{
            Collections.rotate(list, -1);
        }
        return list.toIntArray()
    }
}