def solution(num_list):
    idx=0
    for i in num_list:
        if i<0:
            return idx
        else:
            idx+=1
    return -1