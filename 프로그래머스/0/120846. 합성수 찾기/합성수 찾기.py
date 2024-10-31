def solution(n):
    answer = 0
    
    for x in range(1,n+1):
        count = 0
        for y in range(1,x+1):
            if x%y==0:
                count+=1
                # print(x,y, count)
                if count>=3:
                    answer+=1
                    break
            
    return answer