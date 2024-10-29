def solution(str1, str2):
    answer = 2
    print(str1.count(str2))
    if str1.count(str2) >= 1:
        answer = 1
    
    return answer