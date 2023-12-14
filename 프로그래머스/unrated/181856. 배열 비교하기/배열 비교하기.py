def solution(arr1, arr2):
    answer = 0
    
    #배열길이로 비교
    if len(arr1)<len(arr2): 
        return -1
    elif len(arr1)>len(arr2): 
        return 1
    
    #배열길이가 같은경우 원소의합 비교
    else:
        if(sum(arr1)>sum(arr2)):
            return 1
        elif(sum(arr1)<sum(arr2)):
            return -1
        
    return answer