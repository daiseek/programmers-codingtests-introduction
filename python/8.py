# https://school.programmers.co.kr/learn/courses/30/lessons/120829

def solution(angle):
    answer = 0
    
    if angle > 0 and angle < 90:
        answer = 1
    if angle == 90:
        answer = 2
    if angle > 90 and angle < 180:
        answer = 3
    if angle == 180:
        answer = 4
    
    return answer