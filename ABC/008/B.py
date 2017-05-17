import statistics
n = int(input())
s = []
for i in range(n):
    s.append(str(input()))
count = 1
max = 0
name = s[0]

if n == 1:
    print (s[0])
else:
    s.sort()
    s.append('')
    for i in range(n):
        if s[i] == s[i+1]:
            count += 1
        else:
            if max < count:
                max = count
                name = s[i]
            count = 1
    print (name)
    print (s)
