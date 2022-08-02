a = open("replace.txt" , "w")

a.write("Hello!\n")
a.write("My Name is prarthana nagpal\n")
a.write(":)")

a.close()

a = open("replace.txt" , "r")

s = a.read()

l = list(s)

print(l)
print()

a.close()

a = open("replace.txt" , "w")
for i in range(len(l)) :
    if l[i] == 'a':
        l[i] = "#"
    a.write(l[i])

for i in range(len(l)) :
    print(l[i] ,end="")

a.close()