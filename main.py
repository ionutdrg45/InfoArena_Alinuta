read = open("alinuta.in", "r")
write = open("alinuta.out", "w")

nmax = 50000
poz = [0]*(nmax+5)
d = 1

first_player = 0;

line = read.readline()
line_arr = line.split()
k = int(line_arr[0])
t = int(line_arr[1])

for i in range(1, nmax):
    if poz[i] == 0:
        poz[i] = i + d + k
        if i + d + k <= nmax:
            poz[i + d + k] = i
        d += 1
        d += k

for i in range(0, t):
    line = read.readline()
    line_arr = line.split()
    x = int(line_arr[0])
    y = int(line_arr[1])
    if poz[x] == y:
        write.write("B\n")
    else:
        write.write("A\n")

read.close()
write.close()