def main ():
    num_list = []
    for i in range(5):
        num_list.append(int(input("Please Enter a number")))

    print("The first number is ", num_list[0])
    print("The last number is ", num_list[-1])
    print("The smallest number is ", min(num_list))
    print("The largest number is ", max(num_list))
    print("The average of the numbers is ", sum(num_list) / len(num_list))

main()
