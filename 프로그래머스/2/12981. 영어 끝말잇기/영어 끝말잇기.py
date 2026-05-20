def solution(n, words):
    list=[words[0]]
    for i in range(len(words)-1):
        if(words[i][-1]==words[i+1][0] and words[i+1] not in list):
            list.append(words[i+1])
        else:
            idx=i+1
            return [(idx%n)+1,idx//n+1]
    return [0,0]