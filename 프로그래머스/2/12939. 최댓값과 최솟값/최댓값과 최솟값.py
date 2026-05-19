def solution(s):
    list = s.split()
    return str(min(map(int,list)))+' '+str(max(map(int,list)))