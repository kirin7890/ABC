a, b, x = map(int, input().split())
ans = (b // x) - (max(a-1, 0) // x)
if a == 0:
    ans += 1
print(ans)
