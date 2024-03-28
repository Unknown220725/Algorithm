def solution(arr, intervals):
    answer = []
    
    for x in range(len(intervals)):
        #배열에서 데이터뽑기
        for i in arr[intervals[x][0]:intervals[x][1]+1]: 
            answer.append(i)

    return answer