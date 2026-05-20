def solution(arr):
    answer = [arr[0]]
    idx=0
    for i in range(len(arr)):
        if(arr[i] != answer[idx]):
            answer.append(arr[i])
            idx+=1
    return answer        
    