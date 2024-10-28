def solution(my_string, num1, num2):
    answer = ''
    
    for x in range(len(my_string)):
        
        if x == num1:
            answer += my_string[num2]
        
        elif x == num2:
            answer += my_string[num1]
            
        else:
            answer += my_string[x]

    return answer