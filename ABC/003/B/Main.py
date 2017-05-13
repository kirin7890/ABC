s = raw_input()
t = raw_input()

ac = ['a', 't', 'c', 'o', 'd', 'e', 'r', '@']
def check(x):
    if x in ac:
        return True
    else:
        return False

def eqat(x):
    if x == '@':
        return True
    else:
        return False

for i in xrange(len(s)):
    if s[i] != t[i]:
        if not ((eqat(s[i]) and check(t[i])) or (eqat(t[i]) and check(s[i]))):
            print 'You will lose'
            quit()
print 'You can win'
