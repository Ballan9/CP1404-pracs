LOWER = 33
UPPER = 127

print("Enter a character:")
character = input()
print("The ASCII code for g is", ord(character))
number = int(input("Enter a number between {} and {}:".format(LOWER,UPPER)))
if number < LOWER or number > UPPER:
    print("Invalid number entered")
else:
    print("The Character for {} is ".format(number), chr(number))
for i in range (LOWER,UPPER+1):
    print("{:<3}, {:>3}".format(i, chr(i)))

