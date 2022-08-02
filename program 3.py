a = open("Vowels.txt" , "w")

a.write("Hello!\n")
a.write("My Name is Niranjan Chhawdi\n")
a.write(":)")

a.close()

a = open("Vowels.txt" , "r")

b = a.read()

vowel = 0

for i in b :
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" :
        print(i)
        vowel += 1
print(vowel)

a.close()
