def solution(arr, queries):
    answer = []
    
    for s,e in queries:
        for x in range(s,e+1):
            arr[x] = arr[x]+1
    
    return arr