# https://school.programmers.co.kr/learn/courses/30/lessons/120903

def solution(s1, s2):
    answer = 0
    lessList = []
    largerList = []
    
    if len(s1) > len(s2):
        lessList = s2
        largerList = s1
    else:
        lessList = s1
        largerList = s2
    
    
    for i in range(len(lessList)):
        for j in range(len(largerList)):
            if lessList[i] == largerList[j]:
                answer += 1
        
    
    return answer