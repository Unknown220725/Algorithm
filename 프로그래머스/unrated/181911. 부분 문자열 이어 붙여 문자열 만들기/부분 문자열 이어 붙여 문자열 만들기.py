def solution(my_strings, parts):
    answer = ''
    
    for i in range(len(parts)):
        x,y = parts[i]
        answer += my_strings[i][x:y+1]
    
    return answer