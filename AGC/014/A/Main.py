n = map(int, raw_input().split())
m = [0, 0, 0]


count = 0
while True:
    for i in range(3):
        if n[i]%2 == 1:
            print count
            exit()
    if n[0] == n[1] and n[1] == n[2]:
        print -1
        exit()
    for i in range(3):
        m[i]=(n[(i+1)%3]/2)+(n[(i+2)%3]/2)
    for i in range(3):
        n[i] = m[i]
    count += 1

# a b c
# b/2+c/2 a/2+c/2 a/2+b/2
#
#
