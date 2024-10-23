def solution(n):
    answer = 0
    
    for x in range(n):        
        if n == x*x:
            answer = 1
            break
            
        else:
            answer = 2
    
    return answer