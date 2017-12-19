abcd = list(input())

o = [1, 1, 1]
o2 = []
# print(abcd)
for i in range(2):
    o[0] *= -1
    for j in range(2):
        o[1] *= -1
        for k in range(3):
            o[2] *= -1
            ans = int(abcd[0]) + int(abcd[1])*o[0] + int(abcd[2])*o[1] + int(abcd[3])*o[2]
            # print(ans, i, j, k)
            if ans == 7:
                for l in o:
                    if l > 0:
                        o2.append('+')
                    else:
                        o2.append('-')
                print(abcd[0] + o2[0] + abcd[1] + o2[1] + abcd[2] + o2[2] + abcd[3] + '=7')
                quit()
