def solution(myString, pat):
    answer = 0
    
    myString = myString.lower()
    pat = pat.lower()
    
    if (len(myString)>=len(pat) and myString.find(pat)>-1 ):
        return 1        
    
    
    
    return answer