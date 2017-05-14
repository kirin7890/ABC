n ,m = map(int, input().split())
a = []
b = []
c = []
d = []
for i in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
for i in range(m):
    x, y = map(int, input().split())
    c.append(x)
    d.append(y)

for i in range(n):
    ans = 0
    for j in range(m):
        dist = abs(a[i]-c[j]) + abs(b[i]-d[j])
        if dist < abs(a[i]-c[ans]) + abs(b[i]-d[ans]):
            ans = j
    print (ans+1)
