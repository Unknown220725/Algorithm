def solution(arr, query):
    answer = []
    
    for x in range(len(query)):
        # print(x)
        #짝수
        # print(query[x])
        if (x + 1)%2  == 1 :
            # print("홀")
            # print(arr[:query[x]+1])
            arr = arr[:query[x]+1]
        else:
            # print("짝")
            # print(arr[query[x]:])
            arr = arr[query[x]:]
    
    
    
    return arr