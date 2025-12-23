N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(input()))

answer = 10**9  # 충분히 큰 값

# 8×8 시작 위치
for i in range(N - 7):
    for j in range(M - 7):

        # 시작 색 2가지 경우
        for start in ['W', 'B']:
            count = 0

            # 8×8 내부 검사
            for x in range(i, i + 8):
                for y in range(j, j + 8):
                    if (x + y) % 2 == 0:
                        expected = 'W' if start == 'W' else 'B'
                        if board[x][y] != expected:
                            count += 1                        
                    else:
                        expected = 'B' if start == 'W' else 'W'
                        if board[x][y] != expected:
                            count += 1 

            answer = min(answer, count)

print(answer)
