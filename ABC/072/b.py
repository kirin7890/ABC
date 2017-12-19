ans, n = 0, int(input())
for i in range(n):
    l, r = map(int, input().split())
    ans += r - l + 1
print(ans)
