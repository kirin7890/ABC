c = [[0 for i in range(4)]for j in range(4)]

for i in range(4):
    c[i] = raw_input().split()

for i in range(4):
    for j in range(4):
        print c[3-i][3-j],
    print ""
