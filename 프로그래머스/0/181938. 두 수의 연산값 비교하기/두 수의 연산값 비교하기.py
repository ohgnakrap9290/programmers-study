def solution(a, b):
    return int(str(a)+str(b)) if int(str(a)+str(b)) > 2*a*b or int(str(a)+str(b)) == a*b*2 else a*b*2