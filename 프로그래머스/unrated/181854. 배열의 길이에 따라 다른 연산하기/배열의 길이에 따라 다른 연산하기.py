def solution(arr, n):
    answer = []
    
# result에 나머지 값도 넣어야 하므로 X
#     if len(arr)%2==1:
#         for i in range(0,len(arr),2):
#             print(arr[i]+n)
        
#     else:
#         for i in range(1,len(arr),2):
#             print(arr[i]+n)

    for i in range(len(arr)):
        if(len(arr)%2==1):
            if(i%2==0):
                answer.append(arr[i]+n)
            else:
                answer.append(arr[i])
            
        elif(len(arr)%2==0):
            if(i%2==1):
                answer.append(arr[i]+n)
            else:
                answer.append(arr[i])
            
    return answer