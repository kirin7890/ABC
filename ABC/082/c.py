from collections import Counter
n = int(input())
a = list(map(int, input().split()))
c = Counter(a)
ans = 0
for i, j in c.items():
    if i > j:
        ans += j
    elif i < j:
        ans += (j - i)
print(ans)
