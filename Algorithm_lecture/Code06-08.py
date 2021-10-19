# -*- coding: utf-8 -*-
## 스택

## 함수
def isStackFull():
    global SIZE , stack, top
    if (top >= SIZE -1) : # 꽉찬경우
        return True
    
    else :
        return False


def push(data) :
    global SIZE, stack, top
    if (isStackFull()) : # true 인 경우 
        print('스택 꽉!')
        return
    top += 1
    stack[top] = data

def isStackEmpty() :
    global SIZE, stack, top
    if (top == -1) :
        return True
    else :
        return False

def pop() :
    global SIZE, stack, top
    if (isStackEmpty()) :
        print('스택 텅!')
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek() :
    global SIZE, stack, top
    if (isStackEmpty()) :
        print('스택 텅!')
        return None
    return stack[top]


## 전역
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1

## 메인

# stack = ['커피1', '커피2', '커피3', '커피4', '커피5']
# top = 4
# print(isStackFull())

push('커피1');push('커피2');push('커피3');
push('커피4');push('커피5');
print(stack)
push('커피6')


push('커피1');push('커피2')
print(stack)
print(pop());print(pop());print(pop())

print(peek())
print(stack)
