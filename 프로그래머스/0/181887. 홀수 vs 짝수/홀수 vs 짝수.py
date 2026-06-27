def solution(num_list):
    odd_sum = sum(num_list[0::2])  # 1, 3, 5번째 원소 (인덱스 0, 2, 4...)
    even_sum = sum(num_list[1::2]) # 2, 4, 6번째 원소 (인덱스 1, 3, 5...)
    return max(odd_sum, even_sum)