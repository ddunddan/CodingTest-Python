n = input()

if n.strip() == "":
    print(0)

else:
    count = 0
    for i in range(1, len(n)-1):
        if n[i] == " ":
            count += 1
    print(count + 1)