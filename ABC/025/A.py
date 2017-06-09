s = list(str(input()))
n = int(input())
s.sort()
count = 0
for i in range(len(s)):
    for j in range(len(s)):
        count += 1
        if count == n:
            ans = s[i]+s[j]
print(ans)