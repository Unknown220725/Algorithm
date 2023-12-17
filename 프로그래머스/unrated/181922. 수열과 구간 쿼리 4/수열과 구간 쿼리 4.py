def solution(arr, queries):
    answer = []
    

# s e k 0 4 1 // 0 3 2 // 0 3 3 i대해 i가 k의 1,2,3배수이면 arr[i]에 1을더함
# 0,1,2,4,3 시작
# 1,2,3,5,4 1의배수
# (2,2,4,5),4 2의배수
# (3,2,4,6),4 3의배수

    for j in range(len(queries)):
        for i in range(queries[j][0],queries[j][1]+1):
            if(i%queries[j][2]==0):
                arr[i] += 1
    return arr