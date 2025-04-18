# https://school.programmers.co.kr/learn/courses/30/lessons/120908

def solution(str1, str2):
    answer = 0
    
    if str2 in str1:
        answer = 1
    else:
        answer = 2
    
    return answer

# 문자열은 시퀀스형 자료형이다
# 따라서 순서가 있기에 인덱싱과 슬라이싱이 가능하다
