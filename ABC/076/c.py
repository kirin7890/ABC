s = list(input())
t = list(input())

def eq(s, t):
    for i in range(len(s)):
        if s[i] != t[i] and s[i] != '?':
            return False
    return True

for i in reversed(range(len(s) - len(t)+1)):
    if eq(s[i:i+len(t)], t[:]):
        s[i:i + len(t)] = t[:]
        ans = ''.join(s)
        print(ans.replace('?', 'a'))
        quit()
print('UNRESTORABLE')
