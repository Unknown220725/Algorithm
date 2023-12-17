def solution(myString, pat):
    myString = list(myString)
    
    for i in range(len(myString)):
        if (myString[i] == 'A'):
             myString[i] = 'B'
        else:
             myString[i] = 'A'   
                
    myString = ''.join(myString)
    #print(myString)
    
    # String 타입 문자열 수정을 위해 리스트처럼 인덱스로 접근은 할 수 있지만 수정은 불가능한 것이다
    #myString = myString.replace('B','C').replace('A','B').replace('C','A')    
    # list() 함수 이용
    #myString.split() # split() 함수 이용
    #print(list(myString))
    #     myString = myString.replace('A','B').replace('B','A')
    #     print(myString)
    # for i in range(len(list(myString))):
    #     myString.replace('A','B').replace('B','A')
    #     print(myString[i])
            
    return 0 if myString.find(pat)<0 else 1 