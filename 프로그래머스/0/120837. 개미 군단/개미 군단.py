def solution(hp):
    answer = 0
    if hp%5==0 :
        answer += hp/5 
        return answer
    else:
        answer += int(hp/5) # 4
        hp = hp%5 # 3
    
    if hp%3==0 : # 3 
        answer += hp/3 # 1
        return answer
    else:
        answer += int(hp/3)
        hp = hp%3
        
    if hp!=0:
        answer += hp
        
    return answer