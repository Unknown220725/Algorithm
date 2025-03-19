def solution(my_string, indices):
    answer = []
    list_string = list(my_string)
    
    for x in indices:
        list_string[x] = " "
    
    answer = ''.join(list_string).replace(" ","")
    
    return answer