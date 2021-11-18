## 이진 탐색 트리

## 함수
class TreeNode() :
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

## 전역
memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '에이핑크','걸스데이', '트와이스', '마마무']

## 메인
node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:] : # ['레드벨벳', '에이핑크'...
    node = TreeNode()
    node.data = name

    current = root  # 현재 작업 중인 노드
    while True : # 자리를 몇번만에 잡는지 모름?
        if name < current.data :
            if current.left == None :
                current.left = node
                break
            current = current.left
        else :
            if current.right == None :
                current.right = node
                break
            current = current.right

    memory.append(node)

print('이진 탐색 트리 완료!')

findName = '바마무'
current = root
while True :
    if current.data == findName :
        print(findName, ' 찾음 ^^')
        break
    elif current.data > findName :
        if current.left == None :
            print(findName, '없음 ㅠ')
            break
        current =current.left
    else :
        if current.right == None :
            print(findName, '없음 ㅠ')
            break
        current =current.right
