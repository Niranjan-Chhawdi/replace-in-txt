f = open("timepass.txt" , "a")

a = input("Enter the String : ")

l = list(a)

for i in range(len(l)) :
    print(ord(l[i]))
    print(chr(ord(l[i])))
    f.write(l[i]+ "  : " + str(ord(l[i])) + "\n")

f.close()

