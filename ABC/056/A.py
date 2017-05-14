a, b = map(str, input().split())
if a == 'H':
    ac = 1
else:
    ac = -1
if b == 'H':
    tcd = 1
else:
    tcd = -1

if ac * tcd > 0:
    print ('H')
else:
    print ('D')
