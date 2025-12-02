def solution(strings, n):
    answer = []
    answer2 = []
    for i in range(len(strings)):
        answer.append(strings[i][n]+strings[i])
    answer.sort()
    for i in range(len(answer)):
        answer2.append(answer[i][1:])
        
    return answer2