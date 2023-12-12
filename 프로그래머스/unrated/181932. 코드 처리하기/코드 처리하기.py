def solution(code):
    ret = ''
    mode = 0
    
    for i in range(len(code)):
        if mode == 0 :
            if code[i] == '1':
                mode = 1
            
            elif i%2==0 and code[i]!=1:
                ret += code[i]
            
        elif mode == 1 :
            if code[i]== '1':
                mode = 0
            
            elif i%2==1 and code[i]!=1:
                ret += code[i]
       
    if(ret==""):
        return "EMPTY"
        
    return ret



