def solution(l, r):
    answer = []    

    for i in range(l,r+1): #5~555
#자리수로 5또는 0 합친 크기와 i의 크기가 동일하면 사용 count갯수와 동일하면
        if(str(i).count('5')+str(i).count('0')==len(str(i))):
            answer.append(i)
        
    
    answer.sort()
    
    if(answer==[]):
        answer.append(-1)
    
    return answer