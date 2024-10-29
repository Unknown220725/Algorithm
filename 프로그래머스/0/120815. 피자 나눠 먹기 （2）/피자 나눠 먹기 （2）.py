def solution(n):
    answer = 0
    # box = 0
    
    while(True):
        answer += n
        if(answer%6==0):
            answer = int(answer/6)
            break
    
    return answer