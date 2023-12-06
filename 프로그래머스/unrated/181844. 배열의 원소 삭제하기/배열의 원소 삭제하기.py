def solution(arr, delete_list):
    answer = []    
    answer += arr

    for i in range(len(arr)):
        for j in range(len(delete_list)):    
            if arr[i]==delete_list[j]:
                print(i,arr[i],j,delete_list[j],"동일원소확인")
                answer.remove(arr[i])
                #print(arr, delete_list, answer)

    return answer