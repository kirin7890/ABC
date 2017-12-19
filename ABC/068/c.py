n, m = map(int, input().split())
s, e = set(), set()
for i in range(m):
    a, b = map(int, input().split())
    if a == 1:
        s.add(b)
    elif b == n:
        e.add(a)
if len(s & e) != 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
