def solution(n):
    answer = 0
    
    
    for x in range(1,n+1):
        if (x*x) == n :
            answer = (x+1)*(x+1)
            break
        else :
            answer = -1
    
    
    return answer