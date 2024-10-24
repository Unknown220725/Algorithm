def solution(n, t):
    answer = 0
    for x in range(t+1):
        if answer == 0 :
            answer = n
            print(answer)
        else :
            answer = answer*2
            print(answer)
    return answer