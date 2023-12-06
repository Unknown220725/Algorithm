def solution(num_list, n):
    answer = []
    
    for i in range(len(num_list)):
        print(i+1,"==========",n)
        if i+1>=n:
            answer.append(num_list[i])
        
    return answer