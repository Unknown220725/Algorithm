def solution(rsp):
    answer = ''
    
    for x in rsp:
        print(int(x))
        
        if int(x)==0:
            print("동작중")
            answer+=str(5)
        elif int(x)==2:
            print("동작중")
            answer+=str(0)
        elif int(x)==5:
            print("동작중")
            answer+=str(2)
        print(answer)
    return answer