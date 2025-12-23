max_val = -1
row = 0
col = 0

for i in range(9):
    line = list(map(int, input().split()))
    for j in range(9):
        if line[j] > max_val:
            max_val = line[j]
            row = i + 1
            col = j + 1

print(max_val)
print(row, col)
