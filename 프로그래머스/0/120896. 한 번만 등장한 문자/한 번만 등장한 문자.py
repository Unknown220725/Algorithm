def solution(s):
    answer = ''
    box = []
    
    for x in set(s):  
        if s.count(x) == 1:
            box.append(x)
    
    box.sort()
    
    for y in box:
        answer += y
    
    return answer