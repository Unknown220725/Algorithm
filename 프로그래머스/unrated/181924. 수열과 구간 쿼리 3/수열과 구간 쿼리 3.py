def solution(arr, queries):
    answer = []
    temp = 0
    
    # for i in range(len(queries)):
    #     x,y = queries[i]
    #     temp = arr[x]
    #     arr[x] = arr[y]
    #     arr[y] = temp
    
    for a,b in queries:
        #   0      3      3      0
        arr[a],arr[b]=arr[b],arr[a]

    answer = arr
    return answer

  