def solution(s):
    answer = ""
    ch = ""
    alp = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    
    for i in s:
        if i.isdigit():
            answer += str(i)
        else:
            ch += i
            if ch in alp:
                answer += str(alp.index(ch))
                ch = ""
                
    
    return int(answer)