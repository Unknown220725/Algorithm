def solution(arr, idx):
    answer = 0
    #print(len(arr)-1)
    #answer = -1
    
    for i in range(idx,len(arr)):
        #idx 3 == 3 같은 위치이며 arr[i]가 1일경우 현재 위치 result

        if(arr[i]==1):
            answer = i
            break
        elif(idx<i and arr[i]!=1):
            answer = -1
        
            
#         elif(arr[i]==1 and i==len(arr)-1):
#             answer = i
        

            
            
    return answer