def solution(my_string, queries):
    answer = ''
    
    for x,y in queries:
        reverse_name = ''
        for c in my_string[x:y+1]:
            reverse_name = c + reverse_name
            
        #print(my_string[:x], reverse_name,my_string[y+1:])
        my_string = my_string[:x] + reverse_name + my_string[y + 1 :]
        #print(my_string)
        #my_string
        #my_string = my_string.replace(my_string[x:y+1],reverse_name)
    
    
    return my_string