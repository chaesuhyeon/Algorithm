# python List로 구현

class Queue():
    def __init__(self):
        self.queue=[]
        
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        dequeue_object = None
        if self.isEmpty():
            print("Queue is Empty")
        else:
            dequeue_object = self.queue[0]
            self.queue = self.queue[1:]
            
        return dequeue_object
    
    def peek(self):
        peek_object = None
        if self.isEmpty():
            print("Queue is Empty")
        else:
            peek_object = self.queue[0]
            
        return peek_object
    
    def isEmpty(self):
        is_empty = False
        if len(self.queue) == 0:
            is_empty = True
        return is_empty
    

# 링버퍼를 사용하여 큐 구현
# 고정 길이 큐 클래스 FixedQueue구현하기 
from typing import Any

class FixedQueue:
    class Empty(Exception): # Exception 클래스를 상속 받아서 직접 예외 구현
        """ 비어있는 FixedQueue에서 디큐 또는 피크할 때 내보내는 예외처리 """
        pass
    
    class Full(Exception):
        """ 가득차있는 FixedQueue에서 인큐할 떄 내보내는 예외처리 """
        pass
    
    def __init__(self, capacity:int) -> None:
        """큐 초기화 """
        self.no = 0 # 현재 데이터 개수
        self.front = 0 # 맨앞 원소 커서
        self.rear = 0 # 맨 끝 원소 커서
        self.capacity = capacity # 큐의 크기
        self.que = [None] * capacity # 큐의 본체 
        
    def __len__(self) -> int:
        """큐에 있는 모든 데이트 개수 반환"""
        return self.no
    
    def is_empty(self) -> bool:
        """큐가 비어있는지 판단"""
        return self.no <= 0
    
    def is_full(self) -> bool():
        """큐가 가득차있는지 판단"""
        return self.no >= self.capacity
                    

    def enque(self, x:Any) -> None:
        """데이터 x를 인큐"""
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = x
        self.rear +=1
        self.no +=1
        if self.rear == self.capacity:
            self.rear = 0
    
    def deque(self) -> Any:
        """데이터 x를 인큐"""
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.que[self.front]
        self.front += 1
        self.no -=1
        if self.front == self.capacity:
            self.front = 0
        return x
        
    def peek(self) -> Any:
        """ 큐에서 맨 앞 데이터를 들여다봄 """
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]
    
    def find(self, value:Any) -> Any :
        """큐에서 value를 찾아 인덱스를 반환 (없으면 -1반환)"""
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                return idx
        return -1
    
    def count(self, value:Any) -> bool:
        """큐에서 있는 value의 개수를 반환"""
        c = 0
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                c += 1
        return c
    
    def __contains__(self, value:Any) -> bool:
        """큐에 value가 있는지 판단 """
        return self.count(value)
    
    def clear(self) -> None:
        """큐의 모든 데이터를 비움 """
        self.no = self.front = self.rear = 0
        
    def dump(self) -> None:
        """모든 데이터를 맨 앞부터 맨 끝 순으로 출력 """
        if self.is_empty():
            print("큐가 비었습니다")
        else:
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end='')
            print()
            
            
# 큐 FixedQueue 클래스를 사용한 예   
from enum import Enum

Menu = Enum('Menu', ['인큐', '디큐', '피크', '검색', '덤프', '종료'])

def select_menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end = '')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n) # <Menu.인큐: 1>

q = FixedQueue(64)
            
while True:
    print( f'현재 데이터 개수 : {len(q)}/{q.capacity}')
    menu = select_menu()
    
    if menu == Menu.인큐:
        x  = int(input('인큐할 데이터를 입력하세요 : '))
        try :
            q.enque(x)
        except FixedQueue.Full:
            print('큐가 가득 찼습니다')
            
    elif menu == Menu.디큐:
        try:
            x = q.deque()
            print(f'디큐한 데이터는 {x}입니다.')
        except FixedQueue.Empty:
            print("큐가 비어있습니다")
    
    elif menu == Menu.피크:
        try:
            x = q.peek()
            print(f'피크한 데이터는 {x}입니다.')
        except FixedQueue.Empty:
            print("큐가 비어있습니다")    
    elif menu == Menu.검색:
        x = int(input("검색할 값을 입력하세요"))
        if x in q :
            print(f'{q.count(x)}개 포함되고, 맨 앞 위치는 {q.find(X)} 입니다.')
        else:
            print("검색값을 찾을 수 없습니다")
    
    elif menu == Menu.덤프:
        q.dump()
        
    else:
        break
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        
        

