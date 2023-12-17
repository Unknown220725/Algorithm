def solution(arr):
    stk = []
    i = 0
    
    while(i<len(arr)):
        int_list2 = [int(s) for s in stk]

        if (stk == []):
            #print("case1")
            stk.append(arr[i])
            # print(stk)
            # print(arr[i])
            i+=1
         
        elif(stk!=[] and int_list2[-1] < arr[i]):
            #print("case2")
            stk.append(arr[i])
            # print(stk)
            # print(arr[i])
            i+=1
            
        elif(stk != [] and int_list2[-1] >= arr[i] ):
            #print("case3")
            stk.pop()
            # print(stk)
            # print(arr[i])
        
# 만약 stk가 빈 배열이라면 arr[i]를 stk에 추가하고 i에 1을 더합니다.
# stk에 원소가 있고, stk의 마지막 원소가 arr[i]보다 작으면 arr[i]를 stk의 뒤에 추가하고 i에 1을 더합니다.
# stk에 원소가 있는데 stk의 마지막 원소가 arr[i]보다 크거나 같으면 stk의 마지막 원소를 stk에서 제거합니다.
    
    
    return stk