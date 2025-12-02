def solution(s):
    stack = []
    count = 0
    
    while count < len(s):
        if s[count] == '(':
            stack.append(s[count])
            count += 1
        else:
            if len(stack) == 0:
                stack.append('(')
                count += 1
            else:
                stack.pop()
                count += 1
                
    return len(stack) == 0
            
                
                

        
        
                    