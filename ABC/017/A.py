s = []
for i in range(3):
    a, b = map(int, input().split())
    s.append(a * b * 0.1)
print(int(sum(s)))
