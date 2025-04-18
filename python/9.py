# https://school.programmers.co.kr/learn/courses/30/lessons/120830

def solution(n, k):
    kkochiPrice = 12000
    drinkPrice = 2000
    
    k -= n // 10
    
    answer = kkochiPrice * n + drinkPrice * k
    return answer