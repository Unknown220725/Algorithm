def solution(my_string, s, e):
    
    answer = ''
    answer = list(my_string)

    if s == 0:
        answer[s:e+1] = my_string[e::-1]
    else :
        answer[s:e+1] = my_string[e:s-1:-1]
    
    answer = ''.join(answer)
    
    return answer