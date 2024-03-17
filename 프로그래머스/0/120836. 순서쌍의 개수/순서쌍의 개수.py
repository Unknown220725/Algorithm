def solution(n):
    answer = 0
   
    
    for a in range(1,n+1):  
        if n%a == 0 :
            for b in range(1,n+1):
                if a*b == n:
                    answer += 1
                    break
        else:
            continue
            
                
    return answer