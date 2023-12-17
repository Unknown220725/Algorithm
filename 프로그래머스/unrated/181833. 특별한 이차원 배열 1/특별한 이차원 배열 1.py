def solution(n):
    answer = [[]]
    
    #2차원 배열만들기(얕은 복사 주의 ex. [[raws] * cols])
    arr = [[0 for j in range(n)] for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if (i==j):
                arr[i][j] = 1
                
    
    
    return arr