n = int(input())
a = list(map(int, input().split()))
x = 0
total = sum(a)
ans = []
for i in range(n):
    x += a[i]
    ans.append(abs(x - (total-x)))
ans.pop(-1)
print(min(ans))