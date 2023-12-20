def solution(number):
    answer = 0
    box = list(map(int,number))
    
    # 6 % 9 = 6  
    # 117 + 6 = 123
    
    # 101 % 9 = 2
    # 9 * 8746738469660816943 + 2
    
    return sum(box) % 9