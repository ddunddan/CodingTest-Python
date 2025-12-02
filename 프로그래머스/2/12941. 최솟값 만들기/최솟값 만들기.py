def solution(A,B):
    count = 0
    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        count += A[i] * B[i]
    return count
            