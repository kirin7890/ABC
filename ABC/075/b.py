h, w = map(int, input().split())
s = ['-' * (w + 2)]
for i in range(h):
    s.append('-' + input() + '-')
s.append('-' * (w + 2))

def search(i, j):
    global s
    count = 0
    for l in range(-1, 2):
        for m in range(-1, 2):
            if s[i+l][j+m] == '#':
                count += 1
    return str(count)

for i in range(h + 2):
    for j in range(w + 2):
        if s[i][j] == '.':
            s[i] = s[i].replace('.', search(i, j), 1)
for i in range(1, h + 1):
    print(s[i][1:-1])
