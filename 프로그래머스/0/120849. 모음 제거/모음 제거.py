def solution(my_string):
    answer = ''
    aeiou = ['a','e','i','o','u']
    
    # my_string = list(my_string)
    
    for x in range(len(my_string)):
        # print(my_string[x])
        if my_string[x] == 'a' or my_string[x] == 'e' or my_string[x] == 'i' or my_string[x] == 'o' or my_string[x] == 'u':
            continue
        else:
            answer += my_string[x]
        
            
    return answer