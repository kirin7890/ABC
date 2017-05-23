n, t = map(str, input().split())
s = str(input())

a = str("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

for x in range(int(n)):
    for i in range(26):
        s = s.replace(t[i], a[i])
    s = s.lower()
print(s)
