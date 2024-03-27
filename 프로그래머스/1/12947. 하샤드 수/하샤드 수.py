def solution(x):
    answer = True
    sum_t = 0
    
    for j in str(x):
        sum_t += int(j)
    
    if x%sum_t != 0 :
        return False
    
    return answer