a = list(map(int, input().split()))
b = list(map(int, input().split()))
if a[0] in b or a[1] in b:
    print('YES')
else:
    print('NO')
