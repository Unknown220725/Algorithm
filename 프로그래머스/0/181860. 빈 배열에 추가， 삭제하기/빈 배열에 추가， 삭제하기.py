def solution(arr, flag):
    answer = []
    
    for x in range(len(flag)):
        print(flag[x])
        if flag[x] == True:
            for y in range(arr[x]*2):
                answer.append(arr[x])
            
        else :
            for z in range(arr[x]):
                # print(z)
                answer.pop()
            
    
    return answer