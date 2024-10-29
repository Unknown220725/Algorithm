def solution(box, n):
    answer = 1
    
    for _, x in enumerate(box):
        
        answer = answer * int(x/n)
        print(answer)
        
        
    return answer


# 10 8 6 / 3 3 9 * 3 27

# 324 =  27 * 12

# 480