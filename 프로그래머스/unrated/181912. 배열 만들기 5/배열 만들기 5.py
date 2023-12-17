def solution(intStrs, k, s, l):
    answer = []
    
    # 배열 / s 시작 / l 길이 정수 변환 / k보다 큰값들만 배열 리턴
    
    for i in intStrs:
        if(int(i[s:s+l])>k):
            answer.append(int(i[s:s+l]))
    
    return answer