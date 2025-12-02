def solution(s):
    answer = []
    count = 0
    countz = 0
    
    while s != '1':
        ch = ''
        for i in s:
            if i == '0':
                countz += 1
            else:
                ch += i
                
        a = len(ch)
        
        new = ''
        while a > 0:
            new = str(a % 2) + new              
            a = a // 2
        
        s = new
        count += 1
    
    answer.append(count)
    answer.append(countz)
            
    return answer