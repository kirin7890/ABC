n = int(input())
s = []
p = []
for i in range(n):
    a, b = input().split()
    s.append(a)
    p.append(int(b))
if max(p) > sum(p)/2:
    print(s[p.index(max(p))])
else:
    print('atcoder')
