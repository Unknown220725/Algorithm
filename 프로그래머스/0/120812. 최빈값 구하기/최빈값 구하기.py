
def solution(array):
    answer = 0
    test = 0
    # set 중복제거
    setar = []
    setar = list(set(array))

    # 순회하며 갯수 카운트
    for x in setar:
        t = array.count(x)
        # print(t)
        # answer 보다 t갯수가 큰경우 t 를 answer에 넣기
        if answer < t: # 0 < 1
            answer = t
            test = x
        # answer와 t의 갯수가 동일 할 경우
        elif answer == t: # 2 = 2 
            test = -1
        
        # elif answer >= t:
        #     continue
        # 최빈값 [1,2] 각각 1개일 경우? -1?
    return test