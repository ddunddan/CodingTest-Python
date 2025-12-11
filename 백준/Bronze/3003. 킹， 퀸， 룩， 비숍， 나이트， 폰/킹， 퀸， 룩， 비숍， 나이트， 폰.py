a = list(map(int, input().split()))
b = []

for i in range(2):
    b.append(1-a[i])
for i in range(2, 5):
    b.append(2-a[i])

b.append(8-a[5])

print(*b)
        