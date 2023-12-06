def solution(n):
    
    if (n==1):
        return [[1]]
    
    answer = [[]]
    
    #2차연 배열을 미리 만들어주기
    answer = [[0 for j in range(n)] for i in range(n)]
    
    x = 0
    y = 0
    dir = 'right'    

    for i in range(n*n):
        answer[x][y] = i+1
        print(x,y)
        
        #오른쪽이동
        if(dir=="right"):
            y += 1
            
            # y 3 n-1 3 맨끝 확인 or 이미 값이 있는 경우    
            if y == n-1 or answer[x][y+1] != 0:
                dir ='down'
        #아래이동
        elif(dir=="down"):
            x += 1
            
            if x == n-1 or answer[x+1][y] != 0:
                dir = "left"
        #왼쪽이동        
        elif(dir=="left"):
            y -= 1
            
            if answer[x][y-1] != 0: #y == n-1 or
                dir = "up"
        
        #위로이동
        elif(dir=="up"):
            x -= 1

            if answer[x-1][y] != 0: #x == n-1 or 
                dir = "right"
            
    return answer