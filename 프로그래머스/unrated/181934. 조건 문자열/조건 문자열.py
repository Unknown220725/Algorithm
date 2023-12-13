def solution(ineq, eq, n, m):
    answer = 0    
        
    if(eq=="="):
        answer = int(eval(str(n)+ineq+eq+str(m)))
    
    elif(eq=="!"):
        answer = int(eval(str(n)+ineq+str(m)))
        
    return answer