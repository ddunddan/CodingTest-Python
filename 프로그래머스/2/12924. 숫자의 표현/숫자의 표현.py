def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        count = 0
        a = i
        
        while count < n:
            count += a
            a += 1
            
        if count == n:
            answer += 1
    
    return answer