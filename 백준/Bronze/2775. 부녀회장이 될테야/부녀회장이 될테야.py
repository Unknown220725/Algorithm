# import sys
T = (int)(input()) # test case

for T in range(T):
    
    n = (int)(input()) # test case
    j = (int)(input()) # test case
    
    box = []
    
    for k in range(n+1): # 0층부터 2층까지 이므로 +1
        
        temp = 0
        box.append([]) #2차원으로 만들기 위한 배열추가
        
        for i in range(j):
            
            if k == 0:
                box[k].append(i+1)
                #print(k,"층",i+1,"호")
                #print(box[k][i],"명")
            

            else: 
                temp += box[k-1][i]
                box[k].append(temp)
                #print(k,"층",i+1,"호")
                #print(box[k][i],"명")

    #print(box)
    print(box[k][j-1])