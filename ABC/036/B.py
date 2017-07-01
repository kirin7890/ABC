n = int(input())
s = []
for i in range(n):
    s.append(list(input()))
for i in range(n):
    for j in range(n):
        print(s[n-1-j][i], end='')
    print()