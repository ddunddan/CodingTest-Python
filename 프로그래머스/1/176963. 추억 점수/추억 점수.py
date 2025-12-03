def solution(name, yearning, photo):
    answer = []
    
    for i in photo:
        count = 0
        for j in i:
            if j in name:
                a = name.index(j)
                count += yearning[a]
        answer.append(count)
    
    return answer