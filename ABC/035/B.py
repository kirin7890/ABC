s = input()
t = int(input())
h = abs(s.count('U') - s.count('D'))
w = abs(s.count('R') - s.count('L'))
q = s.count('?')
if t == 1:
    print(h + w + q)
else:
    if h + w - q < 0:
        print(abs(h + w - q) % 2)
    else:
        print(h + w - q)
