def solution(n, arr1, arr2):
    answer = []

    bin1 = [format(x, 'b').zfill(n) for x in arr1]
    bin2 = [format(x, 'b').zfill(n) for x in arr2]

    for i in range(n):
        row = ""
        for j in range(n):
            if bin1[i][j] == "1" or bin2[i][j] == "1":
                row += "#"
            else:
                row += " "
        answer.append(row)

    return answer
