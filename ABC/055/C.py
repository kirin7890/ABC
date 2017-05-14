s, c = map(int, input().split())
ans = 0

if s*2 <= c:
    c -= 2*s
    ans = s
    if c >= 4:
        ans = s + c//4
else:
    ans = c//2

print (ans)
