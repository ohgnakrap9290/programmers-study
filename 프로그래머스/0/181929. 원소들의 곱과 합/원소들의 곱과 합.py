def solution(num_list):
    rhq =1
    wprhq = sum(num_list)**2
    for i in num_list:
        rhq*=i
    return 1 if rhq < wprhq else 0 
    