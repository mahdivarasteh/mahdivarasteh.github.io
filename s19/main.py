f = open("a.txt")
lines = f.readlines()
for i in lines :
    print(i,end="")
f.close()

print(lines)

g = open("b.txt", mode = "w")
for i in lines :
    g.write(i)
g.close()

 