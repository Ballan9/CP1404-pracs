

num_file = open("numbers.txt")

num_list = num_file.read().splitlines()
#print(sum(num_list))

num_total = 0
for i in range(len(num_list)):
    print(type(num_list[i]))
    num_total += int(num_list[i])
print(num_total)
num_file.close()

