def solution(num_list):
    answer = 0
    
    for x in num_list:
        while(True):
            print(answer, x)
            if x==1:
                print("1 종료")
                # answer += 1
                break
        
            elif x%2 == 0:
                print("짝수")
                x = x/2
                print(x)
                answer += 1
                
            elif x%2 == 1:
                print("홀수")
                x = (x-1)/2
                print(x)
                answer += 1
            
            
    
    return answer