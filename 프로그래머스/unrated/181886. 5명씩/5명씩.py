def solution(names):
    answer = []
    y = names
    
    for x in range(len(y)):
        if(int(x%5==0)):
            answer.append(y[x])      
        
    return answer