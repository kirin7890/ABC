n, k = map(int, input().split())
a = []
count = 0

for i in range(n):
    a.append(list(map(int, input().split())))
a = sorted(a, key = lambda x: x[0])
i = 0
while count < k:
    count += a[i][1]
    ans = a[i][0]
    i += 1
print (ans)
