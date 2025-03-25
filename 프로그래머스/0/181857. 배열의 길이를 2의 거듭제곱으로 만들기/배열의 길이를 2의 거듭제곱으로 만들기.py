def solution(arr):
    answer = []
    a = 1
    # 제곱 확인
    while(True):
        if (a==len(arr)):
            break
            
        elif(a>len(arr)):
            break
        a *= 2
        
    # 제곱 만큼 0 추가
    for _ in range(len(arr),a):
        arr.append(0)   
    return arr