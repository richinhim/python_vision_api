f = open('file1.txt', 'w')

for i in range(1,11):
    data = "%d line hello" % i
    f.write(data)

f.close()