def main():
    score = float(input("Enter score: "))
    print(calc_result(score))


def calc_result(score):
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score > 90:
        result = "Excellent"
    elif score > 50:
        result = "Passable"
    else:
        result = "Bad"
    return result

main()