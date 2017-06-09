pi = 3.14159265359
r = []
n = int(input())
for i in range(n):
    r.append(int(input()))
flag = 0
ans = 0
r.sort(reverse=True)
for i in r:
    if flag == 0:
        ans += i**2
        flag = 1
    else:
        ans -= i**2
        flag = 0

print(ans * pi)
