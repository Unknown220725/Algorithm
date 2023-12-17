def solution(arr):
    answer = 1
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            #print(arr[i][j] , arr[j][i])
            if arr[i][j] != arr[j][i]:
                return 0
    
    return answer