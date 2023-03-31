class Solution {
    fun solution(my_string: String): String {
        val strList = my_string.toMutableList()
		
        for(i in strList.indices){
            if(strList[i].isUpperCase()){
            	strList[i] = strList[i].lowercaseChar()
            }
            else{
            	strList[i] = strList[i].uppercaseChar()
            }
        }
        
        return strList.joinToString("")
    }
}