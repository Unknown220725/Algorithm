def solution(my_string, m, c):
    answer = ''
    
#     if m == 1:
#         answer = my_string
    
#     else:
#         for x in range(c-1,len(my_string),m):
#             answer += my_string[x]
            
    return my_string[c-1::m]
    # return answer