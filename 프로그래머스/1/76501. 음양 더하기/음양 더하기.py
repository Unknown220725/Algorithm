def solution(absolutes, signs):
    answer = 0
    
    for i in range(len(signs)):
        #print(signs[i])
        if(signs[i]!=True):
            #print(absolutes[i])
            answer += -(absolutes[i])
            #print(answer)
        else:
            #print(absolutes[i])
            answer += absolutes[i]
            #print(answer)

    return answer