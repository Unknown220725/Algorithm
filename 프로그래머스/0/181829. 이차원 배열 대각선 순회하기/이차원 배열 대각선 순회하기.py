def solution(board, k):
    answer = 0
    
#     #방법 2 count 활용
#     for i in range(len(board)):
#         for j in range(1,k+1):
            
#             # print(board[i].count(j))
#             if board[i].count(j) > 0:
#                 answer += j
#                 # print(j,board[i])
    
    #방법 1 
    for i in range(len(board)):
        for j in range(len(board[i])):          
            print(board[i][j])
            if i+j <= k: #
                # print(board[i][j])
                answer += board[i][j]
                continue
                
                
    
    
    return answer