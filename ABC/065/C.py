n, m = map(int, input().split())
if max(n, m) - min(n, m) > 1:
    p = 0
elif max(n, m) - min(n, m) == 1:
    p = 1
else:
    p = 2
xn, xm = 1, 1
for i in range(1, n + 1):
    xn = (xn * i) % (10 ** 9 + 7)
for i in range(1, m + 1):
    xm = (xm * i) % (10 ** 9 + 7)
ans = (xn * xm * p) % (10 ** 9 + 7)
print(ans)