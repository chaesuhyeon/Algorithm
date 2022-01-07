# 문제 번호 18258 큐 2
import sys

N = int(sys.stdin.readline())
queue = []
idx = 0
for n in range(N):
    menu = sys.stdin.readline().split()

    if menu[0] == "push":
        queue.append(menu[1])
        
    
    elif menu[0] == "pop":
        if len(queue)-idx == 0:
            print(-1)
        else:
            print(queue[idx])
            idx += 1
    
    elif menu[0] == "size":
        print(len(queue)-idx)
    
    elif menu[0] == "empty":
        if len(queue)-idx == 0:
            print(1)
        else:
            print(0)
    
    elif menu[0] == "front":
        if len(queue)-idx == 0:
            print(-1)
        else:
            print(queue[idx])
    elif menu[0] == "back":
        if len(queue)-idx == 0:
            print(-1)
        else:
            print(queue[-1]) 

######################### 처음 풀이 : 시간초과 ########################
import sys
queue = []
N = int(sys.stdin.readline())
for n in range(N):
    menu = sys.stdin.readline().split()

    if menu[0] == "push":
        queue.append(menu[1])
        
    
    elif menu[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue = queue[1:] ######### 이부분때매 시간초과 난듯  / 시간 복잡도를 잘 모르겠음 물어보기 !!
    
    elif menu[0] == "size":
        print(len(queue))
    
    elif menu[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    
    elif menu[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif menu[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1]) 
            
                       
            
            
            


