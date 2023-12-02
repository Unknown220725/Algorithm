def solution(num_list, n):
    answer = []
    
    #012/012 n=2
    #426/176
    #0123/01 n=4
    
    #리스트 0번 2칸 이동 후 데이터 삽입
    
    #0부터 5까지 반복
    for i in range(len(num_list)):
        
        #i가 n을 나눴을때 몫이 0이면 answer에 값을 추가 
        if(i%n==0):
            answer.append(num_list[i]) 
    
    
    return answer