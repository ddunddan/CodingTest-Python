n = str(input())
m = ''
for i in range(len(n)-1,-1,-1):
    m += n[i]
    
if m == n:
    print(1)
else:
    print(0)