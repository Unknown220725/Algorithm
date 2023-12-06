def solution(num_list):
    answer = 0
    temp = 0
    
    for i in range(len(num_list)):
        if i%2==0:
            temp += num_list[i]
            print("temp",temp)
        else:
            answer += num_list[i]
            print("asmwer",answer)
            
    if(temp>answer):
        answer=temp
    
    return answer