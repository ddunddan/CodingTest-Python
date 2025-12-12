word = input().upper()
count = [0] * 26
for i in word:
    count[ord(i)-ord('A')] += 1
    
m = max(count)

if count.count(m) > 1:
    print("?")
else:
    print(chr(count.index(m)+ord('A')))
