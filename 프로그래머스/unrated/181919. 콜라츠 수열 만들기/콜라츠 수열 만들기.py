def solution(n):
    answer = []
    answer.append(n) #10
    
    while(True):
        if(n%2==0): #16 8 4 2 
            n=n/2
            answer.append(n)
        elif(n==1): #1
            break
        else: #5
            n=3*n+1
            answer.append(n)
        
    return answer