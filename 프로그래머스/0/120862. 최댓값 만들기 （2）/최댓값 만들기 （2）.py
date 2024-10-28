def solution(numbers):
    answer = 0
    
    for x in range(len(numbers)): # 0 ~ 4
        for y in range(x+1,len(numbers)): # 1~4
            if answer < numbers[x]*numbers[y] or len(numbers) == 2:
                answer = numbers[x]*numbers[y]

    return answer