def solution(a, b, c):
    answer = 0
    
    if (a!=b and a!=c and b!=c):
        print(a,b,c)
        answer = a+b+c
    
    #elif(a == b and b != c) or (a != b and b == c) or (a != c and c == b):
    
    elif (a==b and a==c and b==c):
        print(a,b,c)
        answer = (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
        
    else:
        print(a,b,c)
        answer = (a+b+c)*(a**2+b**2+c**2)
    
    return answer