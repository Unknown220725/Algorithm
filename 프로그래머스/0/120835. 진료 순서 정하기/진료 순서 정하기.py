def solution(emergency):
    answer = []
    
    for x in range(len(emergency)):
        # print(x)
        count = 0
        for y in emergency:
            # print(emergency[x],y)
            if emergency[x] >= y:
                count+=1
                # print(count)
            
        answer.append(len(emergency)+1-count)
            
        
        
    
    return answer