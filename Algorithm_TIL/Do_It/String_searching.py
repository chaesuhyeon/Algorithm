# 문자열 검색
# 어떤 문자열 안에 다른 문자열이 포함되어 있는지 검사하고
# 만약 포함되어 있다면 어디에 위치하는지 찾아내는 방법
# 문자열 : text / 찾아내는 문자열 : pattern

###################################################################

# 브루트 포스법(=단순법)
# 이미 검사한 위치를 기억하지 못하므로 효율이 좋지 않음

def bf_match(txt: str, pat: str) -> int:
    """브루트 포스법으로 문자열 검색"""
    pt = 0 # txt를 따라가는 커서
    pp = 0 # pat를 따라가는 커서

    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        else:
            pt = pt - pp +1
            pp = 0
    
    return pt - pp if pp == len(pat) else -1 # 문자열이 존재하지 않으면 -1 / 성공하면 성공한 txt 위치의 인덱스를 반환
    # 패턴이 여러개 존재한다면 가장 앞쪽에 위치한 인덱스를 반환 


if __name__ == '__main__':
    s1 = input('텍스트를 입력하세요 : ') # 텍스트용 문자열
    s2 = input('패턴을 입력하세요 : ') # 패턴용 문자열

    idx = bf_match(s1,s2)
    if idx == -1:
        print('텍스트 안에 패턴이 존재하지 않습니다.')
    
    else:
        print(f'{idx+1}번째 문자가 일치합니다.')


###################################################################

# 멤버십 연산자와 표준 라이브러리를 사용한 문자열 검색
# 멤버십 연산자 in과 not in을 사용하면 어떤 문자열이 다른 문자열 안에 포함도어 있는지 검색할 수 있음
# 포함되어있는지는 알 수 있지만 , 위치는 알지 못함

# find 함수 이용
# str.find(sub[, start[,end]]) // start, end 둘다 생략 가능 , sub는 생략 불가
# 문자열 str의 [start : end]에 sub가 포함되면 그 가운데 가장 작은 인덱스를 반환하고, 그렇지 않으면 -1 반환

# rfind 함수 이용
# str.rfind(sub[, start[,end]])
# 문자열 str의 [start : end]에 sub가 포함되면 그 가운데 가장 큰 인덱스를 반환하고, 그렇지 않으면 -1 반환

# index 함수 이용
# str.index(sub[, start[,end]])
# find() 함수와 같은 기능이고, 다만 sub가 발견되지 않으면 예외처리로 ValueError 내보냄

# rindex 함수 이용
# rfind() 함수와 같은 기능을 수행, 다만 sub가 발견되지 않으면 예외처리로 ValueError 내보냄

# with 계열 함수 이용 : 어떤 문자열이 다른 문자열의 시작이나 끝에 포함되어 있는지를 판단함
# start와 end 생략 가능

# startswith 함수 이용
# str.startswith(prefix[, start [, end]])
# 문자열이 prefix로 시작하면 True를 그렇지 않으면 False를 반환함
# start가 지정되어 있으면 그 위치에서 판단을 시작하고,  end가 지정되어 있으면 그 위치에서 비교를 중지함

# endswith 함수 이용
# str.endswith(suffix[, start [, end]])
# 문자열이 suffix로 끝나면 True를 그렇지 않으면 False를 반환함
# start가 지정되어 있으면 그 위치에서 판단을 시작하고, end가 지정되어 있으면 그 위치에서 비교를 중지함

###################################################################

# KMP법
# 브루트 포스법은 일치하지 않는 문자를 만나면 다시패턴의 첫 문자부터 검사를 수행하지만
# KMP법은 검사한 결과를 효율적으로 사용할 수 있는 알고리즘

def kmp_match(txt : str, pat: str) -> int :
    """KMP법으로 문자열 검색"""
    pt = 1 # txt를 따라가는 커서
    pp = 0 # # pat를 따라가는 커서
    skip = [0] * (len(pat) + 1) # 건너뛰기 표

    # 건너뛰기표 만들기
    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] == pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp = skip[pp]

    # 문자열 검색하기
    pt = pp = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]
    return pt - pp if pp == len(pat) else -1


if __name__ == '__main__':
    s1 = input('텍스트를 입력하세요 : ') # 텍스트용 문자열
    s2 = input('패턴을 입력하세요 : ') # 패턴용 문자열

    idx = kmp_match(s1,s2) # 문자열 s1 ~ s2까지를 KMP법으로 검색
    if idx == -1:
        print('텍스트 안에 패턴이 존재하지 않습니다.')
    
    else:
        print(f'{idx+1}번째 문자가 일치합니다.')

###################################################################

# 보이어-무어법
# KMP보다 더 효율적인 방법이고 실제 문자열 검색에서 널리 사용하는 알고리즘
# 패턴의 끝 문자에서 시작하여 앞쪽을 향해 검사를 수행하고,  이 과정에서 일치하지 않는 문자를 발견하면 미리준비한 표를 바탕으로 패턴이 이동하는 값을 결정함
# 패턴에 포함되지 않는 문자를 만난 경우  :  패턴 이동량이 곧 n(패턴 문자열의 길이)
# 패턴에 포함되는 문자를 만난 경우 : 1. 마지막에 나오는 위치의 인덱스가 k이면 이동량은 n-k-1
#                                  : 2. 같은 문자가 패턴안에 중복해서 존재하지 않으면 패턴의 맨 끝 문자의 이동량은 n

def bm_match(txt:str , pat : str) -> int:
    """보이어 무어법으로 문자열 검색"""
    skip = [None] * 256

    # 건너뛰기 표 만들기
    for pt in range(256):
        skip[pt] = len(pat)
    for pt in range(len(pat)):
        skip[ord(pat[pt])] = len(pat) - pt -1

    # 검색하기
    while pt < len(txt):
        pp = len(pat) -1
        while txt[pt] == pat[pp]:
            if pp == 0:
                return pt
            pt -=1
            pp -=1
        pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) - pp \
            else len(pat) - pp

    return -1

if __name__ == '__main__':
    s1 = input('텍스트를 입력하세요 : ') # 텍스트용 문자열
    s2 = input('패턴을 입력하세요 : ') # 패턴용 문자열

    idx = bm_match(s1,s2) # 문자열 s1 ~ s2까지를 KMP법으로 검색
    if idx == -1:
        print('텍스트 안에 패턴이 존재하지 않습니다.')
    
    else:
        print(f'{idx+1}번째 문자가 일치합니다.')
