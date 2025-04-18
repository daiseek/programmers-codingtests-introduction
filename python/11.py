# https://school.programmers.co.kr/learn/courses/30/lessons/120854

def solution(strlist):
    answer = []
    
    for s in range(len(strlist)):
        word = strlist[s]
        wordLenth = len(word)
        answer.append(wordLenth)
        
    return answer