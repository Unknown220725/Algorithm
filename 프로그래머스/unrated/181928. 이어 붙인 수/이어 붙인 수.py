def solution(num_list):
    answer = 0
    box1 = ""
    box2 = ""
    
    for i in range(len(num_list)):
        if(num_list[i]%2==0):
            box1 += str(num_list[i])
        else:
            box2 += str(num_list[i])
            
        print("box1","box2",box1,box2)
    
    
    return int(box2)+int(box1)