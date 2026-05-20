def solution(s):
    list = s.split(' ')
    answer=[]
    for i in list:
        if(i.isdigit()):
            answer.append(i)
        else:
            answer.append(i[:1].upper()+i[1:].lower())
    return ' '.join(answer)