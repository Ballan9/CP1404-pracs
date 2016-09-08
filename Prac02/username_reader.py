username_file = open("name.txt", "r")
username = username_file.read()
print("Your name is {}".format(username))
username_file.close()