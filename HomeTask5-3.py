line = "444555533177"
line2 = ""
for i in range(len(line)):
    n = 1
    while line(i+1) == line(i):
        n = n+1
    line2 = line2+i+n
print(line2)

