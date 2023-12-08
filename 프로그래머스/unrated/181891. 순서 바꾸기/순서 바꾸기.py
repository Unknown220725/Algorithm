def solution(num_list, n):
    answer = []
    
    #print(num_list[n:])
    
#     num_list.append(num_list[n:])
#     print(num_list)
    
    for i in range(n):
        if (i<n):
            num_list.append(num_list[0])
            num_list.remove(num_list[0])
        
    return num_list