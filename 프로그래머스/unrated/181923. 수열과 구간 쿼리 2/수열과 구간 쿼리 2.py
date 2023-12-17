def solution(arr, queries):
    answer = []

    #쿼리즈 길이만큼 반복 3회
    for j in range(len(queries)):
        query = []

        #for i in range(len(arr[queries[j][0]:queries[j][1]+1])): 9점 원인 2시간 소요...
        #arr 슬라이싱 queries[0]~[1]까지 0,4+1
        for i in range(queries[j][0],queries[j][1]+1):
            if arr[i] > queries[j][2]:
                #print(arr[i])
                query.append(arr[i])
            
            #print(queries[j][0],queries[j][1])

            #box.append(arr[i])
           # print(box)
            #2보다 크면 box에 추가
            # if arr[i]>queries[j][2]:
            #     query.append(arr[i])
            #     print(query)
            #    # print("제거")
                
        if(len(query)==0):
            answer.append(-1)
        else:
            answer.append(min(query))
    
    return answer
