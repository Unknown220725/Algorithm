def solution(n):
    answer = []
    
    print(len(str(n)))
    
    for x in range(len(str(n)),0,-1):
 
       answer.append(int(str(n)[x-1:x]))
    
    
    
    return answer