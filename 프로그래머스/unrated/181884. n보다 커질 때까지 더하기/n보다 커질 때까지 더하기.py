def solution(numbers, n):
    answer = 0
    
    for i in numbers:
        answer += int(i)
        if(answer>n):
            break
            print(answer)
    
    return answer