n, k = map(int, raw_input().strip().split())
r = list(map(int, raw_input().strip().split()))
r.sort()
c = 0
for i in xrange(k):
    c = (c + r[n-k+i])/2.0
print c
