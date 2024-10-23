def solution(num, k):
    answer = 0
    
    if str(num).find(str(k))+1 != 0:
        answer =  str(num).find(str(k))+1
    
    else:
        answer = -1
    
    return answer