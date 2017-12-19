s = list(map(int, input().split()))
s.sort()
if s[0] != s[1]:
    print(s[0])
else:
    print(s[2])
