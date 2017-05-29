s = list(str(input()))
n = int(input())
l = []
r = []
temp = ''
for i in range(n):
    l, r = map(int, input().split())
    temp = s[l-1:r]
    temp.reverse()
    s = s[:l-1] + temp + s[r:]
print(''.join(s))
