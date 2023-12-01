def solution(arr, k):
    answer = []
    
    if(k%2==0):
        for x in range(len(arr)):
            answer.append(int(arr[x])+k)
    else:
        for x in range(len(arr)):
            answer.append(int(arr[x])*k)
        
    return answer