def solution(s):
    lst = []
    for i in s:
        if i == '(':
            lst.append('(')
        else:
            if len(lst) == 0:
                return False
            lst.pop() 
    return len(lst) == 0