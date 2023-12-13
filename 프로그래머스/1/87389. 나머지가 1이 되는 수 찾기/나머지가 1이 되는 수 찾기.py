def solution(n):
    answer = 0
    #10%3=1 리턴 3 가장작은 x
    
    for i in range(n,0,-1):
        #print(i,n)
        if(n%i==1):
            answer = i
    
    
    return answer