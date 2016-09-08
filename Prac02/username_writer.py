username_file = open("name.txt", "w")
username = input("Please enter a name: ")
print(username, file=username_file)
username_file.close()