def solution(numbers):
    answer = []
    count = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                count = numbers[i] + numbers[j]
                if count in answer:
                    pass
                else:
                    answer.append(count)
    answer.sort()                
    return answer