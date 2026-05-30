def solution(binomial):
    list = binomial.split()
    if(list[1]=="+"):
        return int(list[0])+int(list[2])
    elif(list[1]=="-"):
        return int(list[0])-int(list[2])
    else:
        return int(list[0])*int(list[2])