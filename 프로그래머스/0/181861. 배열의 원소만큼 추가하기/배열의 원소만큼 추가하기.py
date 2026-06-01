def solution(arr):
    list = []
    for i in arr:
        for j in range(i):
            list.append(i)
    return list