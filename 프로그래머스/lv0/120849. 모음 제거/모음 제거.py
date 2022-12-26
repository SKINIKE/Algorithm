def solution(my_string):
    list_string = list(my_string)
    for i in ["a", "e", "i", "o", "u"]:
        while i in list_string:    
    	    list_string.remove(i) 
    return "".join(list_string)