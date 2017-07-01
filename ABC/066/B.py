s = list(str(input()))
s.pop(-1)
if len(s) % 2 != 0:
    s.pop(-1)
while True:
    if s[:len(s)//2] == s[len(s)//2:]:
        print(len(s))
        break
    s.pop(-1)