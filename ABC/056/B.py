w, a, b = map(int, input().split())

if a+w < b:
    ans = (-(a+w-b))
elif b+w < a:
    ans = a-b-w
else:
    ans = 0
print (ans)
