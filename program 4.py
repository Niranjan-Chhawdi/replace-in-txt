a = open("Vowels.txt" , "w")

a.write("Hello!\n")
a.write("My Name is Niranjan Chhawdi\n")
a.write(":)")

a.close()

a = open("Vowels.txt" , "r")

b = a.read()

s = input("Enter the word to be Searched : ")

for i in b :
    if s == i :
        print(i)

