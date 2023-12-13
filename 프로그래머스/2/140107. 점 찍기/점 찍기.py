# def solution(k, d): #2,4
#     answer = 0
#     box = []
    
#     #0,1,2,3,4 Y축
#     for y in range(d+1):
#         for x in range(0,d+1,k):
#             if(y%k==0 and x+y<=d):
#                 box.append([y,x])
#                 #print(len(box))
#     return len(box)

#사전지식이 없으면 풀기 어려움

#피타고라스의 정리 사전지식
def solution(k, d):
    answer = 0
    for x in range(0,d+1,k):
        res = int((d**2 - x**2)**0.5)
        answer += (res // k) + 1  #y는 0도 가능하므로 +1      
        
    return answer