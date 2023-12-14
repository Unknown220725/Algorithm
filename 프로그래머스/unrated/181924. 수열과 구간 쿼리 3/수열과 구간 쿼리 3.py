def solution(arr, queries):
    answer = []
    temp = 0
    
    for i in range(len(queries)):
        x,y = queries[i]
        temp = arr[x]
        arr[x] = arr[y]
        arr[y] = temp
  
    answer = arr
    return answer