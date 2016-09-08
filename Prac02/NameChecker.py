
outFile = open('name.txt','w')
name = input("What is your name?").upper()
print(name, file=outFile) or outFile.write(name)
outFile.close()

in_file = open("name.txt", "r")
name = in_file.read()
print("Your name is", name)
in_file.close()

# in_file = open("numbers.txt" , "r")
# number1 = int(in_file.readline())
# number2 = int(in_file.readline())
# print(number1 + number2)
# in_file.close()
#
# in_file = open("numbers.txt", "r")