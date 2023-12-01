import sys
from collections import deque

n = int(sys.stdin.readline())
cmd = [sys.stdin.readline().strip() for i in range(n)]

queue = deque()

for j in range(len(cmd)):
    
    if(cmd[j].find('push') != -1):
        push = cmd[j]
        push_sp = push.split(' ')
        queue.append(push_sp[-1])
    
    elif(cmd[j] == "size"):
        print(len(queue))
        
    elif(cmd[j] == "front"):
        if(len(queue) != 0):
            print(queue[0])
        else:
            print(-1)
    
    elif(cmd[j] == "back"):
        if(len(queue) != 0):
            print(queue[-1])
        else:
            print(-1)
    
    elif(cmd[j] == "empty"):
        if(len(queue)==0):
            print(1)
        else:
            print(0)
            
    elif(cmd[j] == "pop"):
        if(len(queue) != 0):
            print(queue[0])
            queue.popleft()
        else:
            print(-1)