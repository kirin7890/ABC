n, m = map(int, input().split())
a = []
b = []

for i in range(m):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

for i in range(n):
    count = 0
    for j in range(m):
        if a[j] == i+1:
            count += 1
        if b[j] == i+1:
            count += 1
    print (count)
