a = map(int, raw_input().split(" "))
A = a[0]
a[1]
a[2]
b = []

while True:
    B = A % a[1]
    if A >= a[1]:
        if (B == a[2]):
            print "YES"
            quit()

        if B in b:
            print "NO"
            quit()
        else:
            b.append(B)
    A += a[0]
