def solution(a, b):
    answer = 0 
    
    if int(str(a)+str(b)) < int(str(b)+str(a)):
        answer = int(str(b)+str(a))    
    elif int(str(a)+str(b)) >= int(str(b)+str(a)):
        answer = int(str(a)+str(b))
    
    
    return answer
    #return int(str(a)+str(b)) if int(str(a)+str(b)) < int(str(b)+str(a)) else int(str(a)+str(b))