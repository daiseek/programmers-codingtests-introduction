# https://school.programmers.co.kr/learn/courses/30/lessons/120806

def solution(num1, num2):
    answer = int ((num1 / num2) * 1000)
    return answer

# 기존에 int 없이 작성했는데 틀림
# 이유가 뭔고 하니, 정수부분만 리턴하는 것이었다
# 그래서 int로 캐스팅함