def main():
    num_of_months = int(input("How many months? "))
    income_list = []

    for month in range(1, num_of_months + 1):
        income_list.append(float(input("Enter income for month " + str(month) + ": ")))
    #.apped means it formats it to string formatting 
    print_report(income_list)


def print_report(income_list):
    print("\nIncome Report\n-------------")
    income_total = 0
    for month in range(len(income_list)):
        income_total += float(income_list[month])
        print(
            "Month {:>2} - Income: ${:>10.2f} Total: ${:>10.2f}".format(month, float(income_list[month]), income_total))
#{:>10 means to right align, .2f is to format to 2 decimal places

main()