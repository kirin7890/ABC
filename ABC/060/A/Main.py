a = map(str, raw_input().split(" "))
first = ""
for i in a:
    if len(first)!=0:
        if i.startswith(first) == False:
            print "NO"
            exit()
    first = i[len(i)-1]
print "YES"
