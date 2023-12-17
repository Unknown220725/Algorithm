def solution(myString):    
    myString = myString.split("x")
    for i in range(len(myString)):
        myString[i] = len(myString[i])
    return myString